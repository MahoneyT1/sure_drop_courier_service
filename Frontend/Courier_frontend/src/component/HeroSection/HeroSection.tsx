import React, { useState } from 'react';
import "./HeroSection.css"


const HeroSection: React.FC = () => {
  const [getInput, setGetInput] = useState("");

  const collectInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    setGetInput(e.target.value);
  };

  return (
      <section className='text-2xl w-[350px]
        h-[50vh] flex flex-col items-center justify-center text-center relative
        md:w-[600px] lg:w-[900px] xl:md-[76vw]'>
        <h1 className='text-white font-Inter backdrop-blur-2xl text-drive-from-left'>Reliable. Fast. Suredrop – Delivering with Care <br />
          Every Time
        </h1>

        <div className='mt-9 relative'>
          <h6 className=' text-2xl text-white backdrop-blur-2xl text-drive-from-right'>Track your goods here</h6>
          <input className='bg-white rounded-lg text-lg w-[250px] h-[35px] mt-5 ps-4
           text-black relative md:w-[400px]' type="text" placeholder='Track Id' value={getInput} onChange={collectInput}
            />
          <button className='text-white text-lg absolute right-1 bg-green-500 w-[100px] top-14 rounded  z-[1]'>Track</button>
        </div>
      </section>
  )
}

export default HeroSection;
