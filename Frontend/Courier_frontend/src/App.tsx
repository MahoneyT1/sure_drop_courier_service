import React from 'react';
import Navbar from './component/Navbar';
import Home from './Pages/Home/Home';
import "./index.css"
import "./App.css"

const App: React.FC = () => {
  return (
    <div className='min-h-screen w-screen overflow-x-hidden bg-sky-550'>
      <Navbar />
      <Home />
    </div>
  )
}

export default App
