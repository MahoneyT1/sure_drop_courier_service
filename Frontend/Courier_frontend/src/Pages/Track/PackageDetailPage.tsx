import React, { useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Locate, Calendar, Package, Truck, User, 
  Bell, PhoneIncoming, CheckCircle, Check, BadgeCheck } from 'lucide-react';
import  "./Track.css"

const PackageDetailPage: React.FC = () => {
    // obtain data in the url
    const navigate = useNavigate();
    const location = useLocation();
    const packageData = location.state?.package;
    console.log('Received package data:', packageData);

    // use useEffect to redirect to the track page if no data is passed
    useEffect(():any => {

        if ( !packageData ) {
            navigate('/track');
        };

    }, [packageData, navigate])

  return (
    <section className='w-full min-h-[150vh] grid grid-cols-1 p-3'>

      {/* Package details section */}
      <div className='mt-10 '>
        <h2 className='text-lg font-bold'>Package Details</h2>

        <div className='flex gap-3 mt-4  
          border-t-1 border-b-1 py-3'>
          <span 
            className='bg-blue-200/30 rounded flex 
            items-center justify-center w-[55px] h-[35px]'>
              <Package size={20}/>
          </span>
          <div>
            <p 
              className='text-primary text-sm font-bold'>
                Package Id: <span className='text-sm font-semibold'>{ packageData.id } </span></p>
            <span className='text-sm '>Shipped on May 15</span>
          </div>

        </div>

        {packageData.deliveries.map((deliveryItem: any, deliveryIndex: number )=> (
          <div key={deliveryIndex} className='min-h-[200vh]'>

            <div className=' flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
          
              <span 
                className='flex justify-center bg-blue-200/30 
                rounded items-center w-[40px] h-[40px]'>
                  <Truck size={20} className='text-gray-800' /> 
              </span> 

              <div className='col-span-1'>
                <p className=' text-primary font-bold'>Shipping Type</p>
                <span className='text-sm text-gray-500'>{deliveryItem.delivery_type}</span>
              </div>
              
            </div>

            <div className='flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
              <span className='flex justify-center bg-blue-200/30
                rounded items-center w-[45px] h-[45px]'>
                  <Calendar size={20} />
              </span>

              <div className=''>
                <p className='text-primary font-bold'>Delivery Date</p>
                <span className='text-sm text-gray-500'>Estimated Delivery: {deliveryItem.delivery_time}</span>
              </div>
              
            </div>

            {/* delivery-status */}
            <div className='flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
              <span className='flex justify-center bg-blue-200/30 
                rounded items-center w-[45px] h-[45px]'>
                <Bell size={20} />
              </span>

              <div className=''>
                <p className='text-primary font-bold'>Delivery Status</p>
                <span className='text-sm text-gray-500'>{deliveryItem.delivery_status}</span>
              </div>

            </div>

            {/* Sender's detail section */}
            <div className='mt-10'>
              <h2 className='text-lg font-bold text-primary'>Sender's Details</h2>

              <div className='flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
                <span className='flex justify-center bg-blue-200/30 
                  rounded items-center w-[45px] h-[45px]'>
                  <User size={20} />
                </span>

                <div className=''>
                  <p className='text-primary font-bold'>Sender's Name</p>
                  <span className='text-sm text-gray-500'>{packageData.user.full_name}</span>
                </div>

              </div>

              <div className='flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
                <span className='flex justify-center bg-blue-200/30 
                  rounded items-center w-[45px] h-[45px]'>
                  <Locate size={20} />
                </span>

                <div className=''>
                  <p className='text-primary font-bold'>Sender's Address</p>
                  <span className='text-sm text-gray-500'>{packageData.user.address}</span>
                </div>

              </div>

              <div className='flex gap-3 mt-6 border-t-1 border-b-1 py-3'>
                <span className='flex justify-center bg-blue-200/30
                  rounded items-center w-[45px] h-[45px]'>
                  <PhoneIncoming size={20} />
                </span>

                <div className=''>
                  <p className='text-primary font-bold'>Phone Number</p>
                  <span className='text-sm text-gray-500'>{packageData.user.phone_number}</span>
                </div>

              </div>
            </div>

            {/* Tracking History */}
            <div className='mt-10 relative'>
              <h2 className='text-lg font-bold'>Tracking History</h2>

              <div className='mt-4 w-full relative '>
                <div className='flex gap-3 box'>
                  <span className=''> <CheckCircle size={15}/> </span>

                  <div className='leading-tight '>
                    <p className='text-sm font-semibold'>Package Delivered</p>
                    <p className='text-sm text-gray-500'>may 18</p>
                  </div>
                </div>
              </div>
            </div>

            
          </div>
          
        ))}
        
      </div>
      

    </section>
  )
}

export default PackageDetailPage
