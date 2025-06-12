import React, { useContext } from 'react';
import ShipmentForm from './ShipmentForm';
import axios from 'axios';
import { toast } from 'react-toastify';
import { AuthContext } from '../../component/Navbar/ToggleLoginLogoutButton';
import { useDownloadReceipt } from './utils'


interface CreateShipmentTypes {
    user: string,
    recipient_name: string,
    recipient_phone_number: string,
    recipient_address: string,
    description: string,
    height: number,
    weight: number,
    length: number,
    width: number,
    pickup_data: string,
    delivery_type: string,
}

const CreateShipment: React.FC = () => {
    const { downloadReceipt, receipt } = useDownloadReceipt();

    // use the context
    const Auth = useContext(AuthContext);

    // create axios instance or config
    const createShipmentApi = axios.create({
        baseURL: 'http://localhost:8000/api/v1/',
        withCredentials: true,
    });

    // handle the create shipment and filter the require and also handle the logics
    const handleOnSubmit = async (data: CreateShipmentTypes)=> {
        
        if ( Auth?.isAuthenticated === true ) {
        try {
            const response = await createShipmentApi.post('package/', data);

            if (response.status === 201 ) {
                toast.success('Successfully created a package');

                // call the download receipt function
                await downloadReceipt(response.data.receipt.id);
            }

       } catch(err) {
        toast.error('error occured, failed to create package');
       };
    }
        
}
    return (
        <section className='w-full min-h-screen bg-primary py-15'>
            {receipt && (
                <div className='text-white text-center p-4 bg-white '>
                    <p className='pb-3 text-2xl lg:text-2xl text-primary font-bold'>Your receipt is ready</p>
                    <a 
                        href={receipt.url} 
                        download={`receipt_${receipt.id}.pdf`}
                        className='text-white p-2 bg-green-500 rounded font-bold'
                        >
                        Download Receipt
                    </a>
                </div>
            )}
            <div className=' p-5'>
                <h1 className='text-green-500 text-4xl text-center font-bold 
                xl:text-5xl '>Ship Your package.</h1>

                <p className='text-white mt-15 text-lg  mx-auto text- max-w-2xl text-center'>Enter your shipment details and we'll handle the rest. Fast
                    , secure, and reliable delivery.
                </p>
            </div>

            <div className='md:px-7 lg:px-35 xl:px-60'>
                <ShipmentForm onSubmit={handleOnSubmit}/>
            </div>
        </section>
  )
}

export default CreateShipment;
