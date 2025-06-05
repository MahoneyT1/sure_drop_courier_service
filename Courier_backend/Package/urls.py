"""
    urls.py for Package
"""

from rest_framework.urls import path
from .views import PackageListCreateView, PackageRetrieveUpdateDestroyView


urlpatterns = [
    path('package/', PackageListCreateView.as_view(), name='package-list-create'),
    path('packages/<uuid:pk>/', PackageRetrieveUpdateDestroyView.as_view(), name='package-detail'),
]
