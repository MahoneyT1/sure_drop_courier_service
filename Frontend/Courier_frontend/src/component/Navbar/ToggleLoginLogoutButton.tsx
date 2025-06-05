import React from 'react';
import { useState, useEffect, createContext } from 'react';
import axios from 'axios'


interface Props {
    children: React.ReactNode
}

interface AuthContextType {
    isAuthenticated: boolean,
    setIsAuthenticated: React.Dispatch<React.SetStateAction<boolean>>,
    checkingAuth: boolean;
    setCheckingAuth: React.Dispatch<React.SetStateAction<boolean>>
};

export const AuthContext = createContext<AuthContextType | null>(null);

const LoginStateContext: React.FC<Props> = ({ children })=> {

    // set component state to monitor users auth
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [checkingAuth, setCheckingAuth] = useState(true);

    // initialize the context provider

    useEffect(()=> {
        const checkAuth = async ()=> {
            try {
                const res = await axios.get('http://localhost:8000/api/v1/auth-verify/', { withCredentials: true});
                    
                if (res.status === 200 ) {
                    console.log("working")
                    setIsAuthenticated(true);
                } else {
                    setIsAuthenticated(false);
                }

            }  catch (err) { 
                setIsAuthenticated(false);
                console.log(err)
            } finally { 
                setCheckingAuth(false) 
            }
        };
        checkAuth();
    }, []);

  return (
      <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated, checkingAuth, setCheckingAuth }}>
        { children }
    </AuthContext.Provider>
  )
}

export default LoginStateContext;
