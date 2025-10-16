/**
 * login page.
 */

import React, { useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import {  toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { AuthContext } from '../../component/Navbar/ToggleLoginLogoutButton';
import axiosInstance from '../../Utils/AxiosInstance';
// import { ReceiptRussianRuble } from 'lucide-react';


interface LoginProps {
    email: string,
    password: string,
}

const Login: React.FC = ()=> {

    // create a navigation object
    const navigator = useNavigate();

    // set up the form object
    const { 
        handleSubmit, 
        register,
        reset,
        formState : { errors, isSubmitting }
        } = useForm<LoginProps>();

    // access the AuthContext
    const Auth = useContext(AuthContext);

    // function to handle login
    const handleLogin = async (formData: LoginProps)=> {

        // login url
        const url = 'login/';

        try {
            // make a post request with login details
            const response = await axiosInstance.post(url, formData, { withCredentials: true});

            if (response.status === 200) {
                toast.success("Successfully logged in", 
                    { onClose: () => navigator('/', { replace: true }),
                     autoClose: 2000
                    });
                }
                // set the isAuthenticated to true in the context
                Auth?.setIsAuthenticated(true);
            
        } catch (err: any) {
            toast.error("check your info or create an account !", {
                autoClose: 2000});
            reset();
            Auth?.setIsAuthenticated(false);
            navigator('/login', { replace: true } );
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
                {   errors.password && 
                        <p className='text-red-500 '>
                            {errors.password.message} 
                        </p>
                }

                <div className='mt-7 w-full'>
                    <button 
                        type='submit'
                        disabled={ isSubmitting } 
                        className='p-3 border bg-green-500
                        text-white rounded-lg w-full text-lg 
                        disabled:opacity-50 disabled:cursor-not-allowed'>
                            { isSubmitting ? 'Logging in...' : 'Login' }
                     </button>
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