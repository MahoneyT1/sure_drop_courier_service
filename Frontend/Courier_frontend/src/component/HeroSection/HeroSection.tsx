import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import "./HeroSection.css";
import { API_BASE_URL } from '../../config';
import axios from 'axios';
import { toast } from 'react-toastify';


interface TrackInput {
  track: string
};


const HeroSection: React.FC = () => {

  const { register, handleSubmit, 
    formState: { errors, isSubmitting }} = useForm<TrackInput>();

  const navigate = useNavigate();

  async function handleTrack (getInput: TrackInput) {

    // call api for tracking 
    const url = API_BASE_URL + 'packages/';

    const { track } = getInput;
      try { 
        const response = await axios.get(
          `${url}${track}/`, { withCredentials: true });

        const packageData = await response.data;
        navigate(`/package-details`, { state: { package: packageData }});

      } catch( err: any) {
        toast.error(err);
      }
    }

  return (
      <section className='text-2xl w-[350px]
        h-[50vh] flex flex-col items-center justify-center text-center relative
        md:w-[600px] lg:w-[900px] xl:md-[76vw]'>
        <h1 className='text-white font-Inter backdrop-blur
          text-drive-from-left lg:text-5xl'>
            Reliable. Fast. Fask-Link – Delivering with Care <br />
            Every Time
        </h1>

      <h6 className=' text-2xl text-white backdrop-blur-2xl
            text-drive-from-right lg:text-4xl '>Track your parcel/Package here
      </h6>

        <div className='mt-9 py-3'>
         
          <form onSubmit={handleSubmit(handleTrack)}
              className='flex justify-center items-center gap-2'>
              <input 
                {...register('track', { required: "Tracking id is required" })}
                className='bg-white rounded-lg text-lg  
                ps-4 py-0 text-black relative md:w-[400px]
                  lg:p-5 '
                name="track" type="text" placeholder='Track Id'
                />
                { errors.track && 
                  <p className='text-white-300 '>{errors.track.message} </p>}
              <button
                type='submit'
                disabled={ isSubmitting }
                className='px-8 py-0 bg-green-600 text-white rounded-lg'>
                  {isSubmitting ? 'Tracking...' : 'Track'}  
                </button>
          
          
          </form>
          
          
        </div>
      </section>
  )
}

export default HeroSection;
