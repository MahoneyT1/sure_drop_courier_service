import React, { useState } from 'react';
import "./HeroSection.css";
import Button from '../Button';


const HeroSection: React.FC = () => {
  const [getInput, setGetInput] = useState("");

  const collectInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setGetInput(e.target.value);
  };

  function handleTrack () {
    // call api for tracking 
    console.log("button pressed");

  }

  return (
      <section className='text-2xl w-[350px]
        h-[50vh] flex flex-col items-center justify-center text-center relative
        md:w-[600px] lg:w-[900px] xl:md-[76vw]'>
        <h1 className='text-white font-Inter backdrop-blur
          text-drive-from-left lg:text-5xl'>
            Reliable. Fast. Suredrop – Delivering with Care <br />
            Every Time
        </h1>

        <div className='mt-9 relative'>
          <h6 className=' text-2xl text-white backdrop-blur-2xl
            text-drive-from-right lg:text-4xl '>Track your parcel here</h6>

          <div className=' relative'>
              <input className='bg-white rounded-lg text-lg  
              h-[35px] mt-5 ps-4 text-black relative md:w-[400px]
              lg:p-5 '
              name="track" type="text" placeholder='Track Id'
              value={getInput} onChange={collectInput}
              />

              <Button buttonName='Track'
                className='bg-green-500
                absolute right-2/50 lg:right-1 top-8 -translate-y-2/6
                lg:top-8 lg:-translate-y-2/7 lg:p-1 rounded text-white
                text-lg md:right-1 md:top-8 md:p-0.5'
                onClickFunc={()=> handleTrack}/>
          
          </div>
          
          
        </div>
      </section>
  )
}

export default HeroSection;
