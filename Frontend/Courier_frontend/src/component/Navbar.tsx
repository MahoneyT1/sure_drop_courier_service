import React, { useState } from 'react'
import { Menu, X } from 'lucide-react';
import suredrop from "../assets/suredrop-logo .png";


const Navbar: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);

  return (
    <header className='w-full bg-primary text-white text-bold-400'>
        <div className="mx-auto md:px-6 flex justify-between items-center">
            {/* logo */}
            <img className='w-16 ' src={suredrop} alt="logo-image" />
            
            {/* Destop Navigation */}
            <nav className='hidden md:flex space-x-6' aria-label='primary navigation'>
                <ul className='flex space-x-15 text-lg'>
                    <li className='hover:text-gray-300'>Home</li>
                    <li className='hover:text-gray-300'>About</li>
                    <li className='hover:text-gray-300'>Contact</li>
                    <li className='hover:text-yellow-300'>Services</li>
                    <li className='hover:text-yellow-300'>Track</li>
                    <li className='hover:text-yellow-300'>Testimonia</li>
                </ul>
            </nav>

            {/* Mobile Menu Button */}
            <button
                onClick={()=> setIsOpen(!isOpen)}
                className='md:hidden'
                aria-label='Toggle Menu'
                aria-controls='Mobile-menu'
                aria-expanded={isOpen}
                >
                    {isOpen ? <X size={28}/> : <Menu size={28}/>}
            </button>
        </div>

        {/* Mobile navigation (hidden on default) */}
        {isOpen && (
            <nav id='mobile-menu' className='md:hidden bg-blue-500 '>
                <ul className='flex flex-col items-center '>
                    <li className='hover:text-yellow-300 py-1'>Home</li>
                    <li className='hover:text-yellow-300 py-1'>About</li>
                    <li className='hover:text-yellow-300 py-1'>Services</li>
                    <li className='hover:text-yellow-300 py-1'>Track</li>
                    <li className='hover:text-yellow-300 py-1'>Testimonia</li>

                </ul>
            </nav>
        )}
    </header>
  )
}

export default Navbar;
