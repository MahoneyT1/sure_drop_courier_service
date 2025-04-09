import React from 'react';
import { useState } from 'react';

const ShippingCalculator: React.FC = () => {
    //input state management
    const [weight, setWeight] = useState("");
    const [length, setLength] = useState("");
    const [width, setWidth] = useState("");
    const [height, setHeight] = useState('');
    const [destination, setDestination] = useState('');
    const [price, setPrice] = useState<number | null>(null);
    const [error, setError] = useState('');
    const [active, setActive] = useState(false);

    const calculateShippingRate = ()=> {

        // reset the error error log and price output
        setError("");
        setPrice(null);
        setActive(!active);

        // validate the inputs
        const weightNum = parseFloat(weight);
        const lengthNum = parseFloat(length);
        const widthNum = parseFloat(width);
        const heightNum = parseFloat(height);

        if (isNaN(weightNum) || widthNum <= 0) {
            setError('Please enter a valid weight');
            return;
        }

        if (isNaN(lengthNum) || isNaN(widthNum) || isNaN(heightNum) || 
            lengthNum <= 0 || widthNum <= 0 || heightNum <= 0 ) {
                setError('Please enter a valid package dimensions');
                return;
        };
        
        // Basic pricing algorithm
        const baseRate = destination === 'domestic' ? 500 : 1000;
        const weightRate = weightNum * 2;
        const volumeRate = (lengthNum * widthNum * heightNum)/1000 * 0.5;

        const totalPrice = baseRate + weightRate + volumeRate;

        setPrice(Math.max(10, Math.round(totalPrice * 100) / 100))
    };

  return (
    <section className='w-[90vw] mt-5 p-4 pb-10 bg-white shadow-[0px_2px_2px_1px_gray] rounded-2xl'>
        <div className='text-center'>
            <h6 className='text-2xl font-semibold'>Shipping Rate Calculator</h6>
        </div>

        <div className='flex flex-col mt-5'>
            <label htmlFor="weight">Weight (kg)</label>
            <input id='weight'
                type="number"
                placeholder='Enter package weight'
                onChange={(e)=> setWeight(e.target.value)}
                className='border-2 border-gray-400 rounded mt-1 p-2'
            />
        </div>

        <div className='grid grid-cols-3 gap-3 mt-3'>
            <div className='w-[100px]'>
                <label htmlFor="length">Length (cm)</label>
                <input id='length' type="number" placeholder='Width'
                onChange={(e)=> setLength(e.target.value)}
                className='border-2 border-gray-400 rounded w-20 text-center' />
            </div>

            <div className='w-[100px]'>
                <label htmlFor="Width">Width (cm)</label>
                <input type="number" placeholder='Width'
                onChange={(e)=> setWidth(e.target.value)}
                className='border-2 border-gray-400 rounded w-20 text-center' />
            </div>

            <div className='w-[100px] '>
                <label htmlFor="Length">Height (cm)</label>
                <input type="number" placeholder='Height'
                onChange={(e)=> setHeight(e.target.value)}
                className='border-2 border-gray-400 rounded w-20 text-center' />
            </div>

            <div>
                <label htmlFor="dom-inter">Domestic</label>
                <select name="dom-inter"
                 id="dom-inter"
                 className='border-2 border-gray-400 w-[650px] rounded p-2'
                 onChange={(e)=> setDestination(e.target.value)}
                 >
                 
                 <option value="domestic">Domestic</option>
                 <option value="international">International</option>

                 </select>
            </div>
        </div>
        <button
            onClick={calculateShippingRate}
            className='border-2 mt-4 rounded w-[260px] p-3 border-gray-400 bg-gradient-to-r from-green-700 to-green-400 text-white'
            
        >
                Calculate Shipping Rate
        </button>

        {error && (
            <div>
                {error}
            </div>
        )}

        {price && (
            <div>
                Estimated shipping cost : <strong>{price.toFixed(2)}</strong>
            </div>
        )}


    </section>
  )
}

export default ShippingCalculator;
