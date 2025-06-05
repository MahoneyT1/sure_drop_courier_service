"""
    This module contains the views for the Package app.
    It defines the API endpoints for creating, retrieving, updating,
    and deleting Package objects.
    It uses Django REST Framework's concrete generic to handle the requests
    and responses.
    The views are designed to be used with the PackageSerializer class
    to serialize and deserialize Package objects.
    The views also include authentication and permission classes
    to ensure that only authorized users can access the endpoints.
"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Package.models import Package
from Package.serializer import PackageSerializer
from Courier.models import Courier
from Courier.serializer import CourierSerializer
from Delivery.models import Delivery
from Delivery.serializer import DeliverySerializer
from Receipt.models import Receipt
from Receipt.serializer import ReceiptSerializer
from Location.models import Location
from Location.serializer import LocationSerializer
from django.template.loader import render_to_string
from rest_framework.exceptions import ValidationError
from django.db.models import Prefetch
from django.utils import timezone
import datetime
import traceback



class PackageListCreateView(ListCreateAPIView):
    """
        Api view for listing and creating Package objects.
        It uses the PackageSerializer class to serialize and deserialize
        Package objects.
    """

    queryset = Package.objects.all()
    serializer_class = PackageSerializer

    def get(self, request, *args, **kwargs):
        """
            Handle GET requests to list all Package objects.
        """
        packages = self.get_queryset()
        serializer = self.get_serializer(packages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
            Handle POST requests to create a new Package object.
        """
        # create a package
        try:
            delivery_type = request.data.pop('delivery_type')
            serializerPackage = PackageSerializer(data=request.data, context={ 'request': request })
            serializerPackage.is_valid(raise_exception=True)
            package = serializerPackage.save(user=request.user)

            # now search for available courier to handle each shipment
            assign_courier = Courier.objects.filter(available=True).first()

            if assign_courier:
                # create a delivery and assign courier and package in it

                pickup_date = serializerPackage.validated_data.get('pickup_date')
                pickup_date_timezone = timezone.make_aware(
                    datetime.datetime.combine(pickup_date, datetime.time.min)
                    )
                try:
                    # create a delivery and to track both courier and the package
                    delivery = Delivery.objects.create(
                        courier=assign_courier,
                        package=package,
                        delivery_type=delivery_type,
                        delivery_time=pickup_date_timezone,
                        delivery_address=serializerPackage.validated_data.get('recipient_address'),
                    )
                    serialized_delivery = DeliverySerializer(delivery)

                    # create a location
                    try:
                        location = Location.objects.create(
                            package=package,
                        )
                        location = location.save()
                        serialized_location = LocationSerializer(location)
                    except Exception as e:
                        print(str(e))
                        return Response(
                            { 'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )

                    # create Receipt
                    try:
                        receipt = Receipt.objects.create(
                            package=package,
                            amount=2000,
                            )
                        try:
                            # render a html template in the attribute of the created Receipt
                            html_string = render_to_string('receipt.html', {'receipt': receipt})
                            receipt.html_content = html_string
                            receipt.save()

                        except Exception as e:
                            traceback.print_exc()
                            return Response(
                                {
                                    "Error": "error occured"
                                }, 
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

                        serialized_receipt = ReceiptSerializer(receipt)
                        return Response(
                            {
                                "success": "successfully shipped your Package",
                                "package": serializerPackage.data,
                                "delivery": serialized_delivery.data,
                                "receipt": serialized_receipt.data,
                                "location": serialized_location.data
                            },
                            status=status.HTTP_201_CREATED
                        )
                    except Exception as e:
                        return Response(
                            {
                                "Error": "error occured"
                            }, 
                            status=status.HTTP_400_BAD_REQUEST
                        )
                except Exception as e:
                    print(str(e))
                    return Response(
                        {
                            "Error": "error occured"
                        }, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response({"Error": "no courier found"}, status=status.HTTP_404_NOT_FOUND)

        except ValidationError as ve:
            print("Validation Error:", ve.detail)
            return Response(
                {
                    "errors": ve.detail
                }, status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            print(str(e))
            return Response(
                {
                    "error": "error serializing data"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )


class PackageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        Api view for retrieving, updating, and deleting Package objects.
        It uses the PackageSerializer class to serialize and deserialize
        Package objects.
    """

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Package.objects.prefetch_related(
            Prefetch(
                'deliveries', queryset=Delivery.objects.select_related('courier')
            )
        ).select_related('user')

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Package.DoesNotExist:
            print("Package with the ID does not exist")
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        """
            Handle PUT requests to update a specific Package object.
        """
        package = self.get_object()
        serializer = self.get_serializer(package, data=request.data)
        serializer.is_valid(raise_exception=True)
        package = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
            Handle DELETE requests to delete a specific Package object.
        """
        package = self.get_object()
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
