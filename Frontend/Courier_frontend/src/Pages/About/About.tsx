import React from 'react';
import SmallCardStats from '../../component/Card/SmallCardStats';
import  { smallData } from "../../component/Card/smallCardData";
import { motion } from 'motion/react';
import { easeIn } from 'motion';

// ABout UI
const About:React.FC = () => {
    
   
  return (
    <section className='bg-white w-full min-h-[100vh] '>
        <div className='lg:px-80 text-center mt-8'>
            <div className='text-lg text-primary font-bold leading-[3.1rem]
                md:text-5xl'>Delivering Trust, <br />
               <span className='text-green-500'>One Package at a Time</span> 
            </div>
            
            <h6 className='mt-7 text-lg text- text-center'>Since 2020, SureDrop has been revolutionizing the
                courier industry with innovation and reliability.
            </h6>
        </div>

        <div className='mt-15 p-3 text-center'>
            <h2 className='text-4xl font-bold text-primary'>Our Story</h2>
            <p className='mt-5 text-lg text-primary '>Born from a vision to transform package delivery,
                SureDrop emerged when our founders recognized the
                need for a more reliable, transparent, and
                customer-focused courier service.
            </p>

            <p className='mt-5 text-lg text-primary '>
                What started as a small local delivery service has
                grown into a trusted nationwide network, connecting
                people and businesses with confidence and care.
            </p>
        </div>

        {/* our mission section */}
        <div className='flex flex-col bg-white md:flex-row justify-between place-items-center w-full py-10'>
            
            <div className='shadow-[2px_2px_4px_gray] m-4 rounded-2xl pb-6 mb-5 flex-1 p-4 mt-10'>
                <div className='m-4 text-center text-4xl '>
                    <i className='fa-solid fa-bullseye bg-gradient-to-b from-primary to-green-500 text-transparent bg-clip-text'></i>
                </div>

                <div className='m-4 text-center mt-5'>
                    <p className='font-bold text-4xl text-primary'>Our Mission</p>
                </div>

                <div className='mt-5 text-center '>
                    <p className='text-center '>
                        To provide exceptional courier services that
                        ace of mind through reliability and innovation.
                    </p>
                </div>
                
            </div>

            <div className='shadow-[2px_2px_4px_gray] m-4 rounded-2xl pb-6 mb-5 flex-1 p-4 mt-10'>
                <div className='m-4 text-center text-4xl'>
                    <i className='fa-solid fa-cube bg-gradient-to-b from-primary to-green-500 text-transparent bg-clip-text'></i>
                </div>

                <div className='m-4 text-center mt-5 text-primary'>
                    <p className='font-bold text-4xl'>Our Vision</p>
                </div>

                <div className='mt-4 text-center'>
                    <p>To become the most trusted name in courier services, 
                        setting new standards for reliability, transparency,
                        and customer satisfaction.
                    </p>
                </div>
                
            </div>
        </div>


        <motion.div className='grid grid-cols-2 gap-8 mt-20 p-3 md:grid-cols-4 bg-white
        '
        initial={{ 
            y: 180,
            opacity: 0
        }}
        
        whileInView={{
            y: 0,
            opacity: 1 ,
        }}
        transition={{
            delay: 0.6,
            duration: 0.2,
            ease: easeIn,
            type: "spring",
            bounce: 0.6
        }}
        >
            {smallData.map((data, index)=> (
                <div key={index} className=' text-center  '>
                    <SmallCardStats icon={data.icon} value={parseInt(data.title)} body={data.body} character={data.character}/>
                </div>
            ))}
        </motion.div>


    </section>
  )
}

export default About;
