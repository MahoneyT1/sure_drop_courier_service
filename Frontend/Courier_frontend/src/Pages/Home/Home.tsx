import React from 'react';
import backgroundImage from "../../assets/HeroBackground.jpg";
import HeroSection from '../../component/HeroSection/HeroSection';
import Features from '../../component/Features/Features';
import ServiceSection from '../../component/ServiceSection/ServiceSection';
import ShippingCalculator from '../../component/ShippingCalculator';
import "./Home.css"

const Home: React.FC = () => {
  return (
    <section className='w-full'>
      <div className='flex justify-center items-center relative w-full min-h-screen overflow-hidden'
        style={{
          backgroundImage: `url(${backgroundImage})`, backgroundSize: "cover",
          backgroundPosition: "center"
        }}>

        <HeroSection />
      </div>


      <div className='w-full flex flex-col justify-center items-center mt-2 px-4 rounded-3xl'>
        <ServiceSection />
      </div>

      <div className='max-w-7xl mx-auto px-4'>
        <Features />
      </div>

      <div className='flex justify-center'>
        <ShippingCalculator/>
      </div>





    </section>

  )
};

export default Home;
