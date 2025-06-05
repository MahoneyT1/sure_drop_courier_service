import React, { useEffect, useState, useContext, useNavigation } from 'react'
import { Menu, X } from 'lucide-react';
import suredrop from "../../assets/suredrop-logo.png";
import {  Link, useNavigate } from 'react-router-dom';
import Button from '../Button';
import { AuthContext } from "./ToggleLoginLogoutButton";
import axios from "axios";
import 'react-toastify/dist/ReactToastify.css';


const Navbar: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    const Auth = useContext(AuthContext);
    const navigateTo = useNavigate();

    // make a request to authenticated route to be sure the user is logged in

    const handleLogout = async () => {

        const res = await axios.post('http://localhost:8000/api/v1/logout/', {}, { withCredentials: true });

        try {
            if (res.status === 200 ) {
                Auth?.setIsAuthenticated(false);
                navigateTo('/');
                // toast("Logged out")
            }
        } catch (err) {
            console.warn(err);
        }
    };

  return (
    <header className='w-full bg-primary text-white text-bold-400'>
     

        <div className="mx-auto md:px-6 flex justify-between items-center">
            {/* logo */}
            <img className='w-16 ' src={suredrop} alt="logo-image" />
            
            {/* Destop Navigation */}
            <nav className='hidden md:flex space-x-6 items-center' aria-label='primary navigation'>
                <ul className='flex space-x-15 text-lg'>
                    <li><Link className='hover:text-gray-300' to="/">Home</Link></li>
                    <li ><Link className='hover:text-gray-300' to="/about">About</Link></li>
                    <li ><Link className='hover:text-gray-300' to="/contact">Contact</Link></li>
                    <li ><Link className='hover:text-yellow-300' to="/service">Service</Link></li>
                    <li ><Link className='hover:text-yellow-300' to="/track">Track</Link></li>
                </ul>
                
                {Auth?.isAuthenticated ? (
                    <Button buttonName='logout' className='bg-green-500 p-1 rounded font-bold'
                    onClickFunc={async ()=> handleLogout()} />
                ): (
                    <Button buttonName='login' className='bg-green-500 to-green-500 p-2 rounded font-bold'
                       linkUrl='/login'/>
                ) }

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

             {/* Mobile navigation (hidden on default) */}
            {isOpen && (
                <nav id='mobile-menu' className='md:hidden bg-blue-500 '>
                    <ul className='flex flex-col items-center '>
                        <li><Link className='hover:text-yellow-300 py-1' to="/">Home</Link></li>
                        <li><Link className='hover:text-yellow-300 py-1' to="/about">About</Link></li>
                        <li><Link className='hover:text-yellow-300 py-1' to="/contact">Contact</Link></li>
                        <li><Link className='hover:text-yellow-300 py-1' to="/service">Service</Link></li>
                        <li><Link className='hover:text-yellow-300 py-1' to="/track">Track</Link></li>
                        
                    </ul>
                </nav>
            )}
        </div>

       
    </header>
  )
}

export default Navbar;
