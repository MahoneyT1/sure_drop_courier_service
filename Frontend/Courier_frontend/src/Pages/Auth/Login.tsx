/**
 * login page.
 */

import React, { useState, useEffect, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import Button from '../../component/Button';
import axios from 'axios';
import {  toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { AuthContext } from '../../component/Navbar/ToggleLoginLogoutButton';


interface LoginProps {
    email: string,
    password: string,
}

const Login: React.FC = ()=> {
    const navigator = useNavigate();
    const { 
        handleSubmit, 
        register, 
        formState : { errors,  }
        } = useForm<LoginProps>();

    const Auth = useContext(AuthContext);


    const handleLogin = async (formData: LoginProps)=> {
        console.log(formData);


        const baseUrl = 'http://localhost:8000/api/v1/login/'

        try {
            // make a post request with login details
            const response = await axios.post(baseUrl, formData, { withCredentials: true});

            if (response.status === 200) {
                toast.success("Successfully logged in");
                Auth?.setIsAuthenticated(true);
                navigator('/', { replace: true })
            }
        } catch (err) {
            toast.error("error occured!");
        }
    };

    return (
        <section className='w-full p-3 md:px-30 md:p-10 lg:px-40 bg-primary min-h-screen'>

            <form onSubmit={handleSubmit(handleLogin)} 
                className='bg-white rounded-2xl p-7 text-primary lg:mx-60'>

                <div className='w-full  text-center '>
                    <h4 className='text-3xl font-bold'>Courier Login</h4>
                </div>

                <div className='py-5 '>
                    <label htmlFor="email" className='w-full block font-bold' >Email</label>
                    
                    <input type="email" 
                    id='email'
                    {...register('email', { required: "Email is required for login" })}
                     className='border-1 rounded-lg w-full p-2 mt-1' />
                </div>
                {errors.email && <p className='text-red-500 '>{errors.email.message} </p>}

                <div>
                    <label htmlFor="password"
                    className='block w-full mt-2 font-bold'>Password</label>
                    <input 
                    type="password"
                    { ...register('password', { required: "Password is required"})}
                    className='border-1 rounded-lg w-full p-2 mt-1' />
                </div>
                {errors.password && <p className='text-red-500 '>{errors.password.message} </p>}

                <div className='mt-7 w-full'>
                    <Button buttonName='Log in' className='p-3 border bg-green-500
                     text-white rounded-lg w-full text-lg' />
                </div>

                <div className='mt-9 lg:text-center'>
                    <p className=''>Don't have an account? 
                        <Link to='/register' className='text-blue-500'> Create one</Link> </p>
                </div>
            
            </form>

        </section>
    )
};

export default Login;