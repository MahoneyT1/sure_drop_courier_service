import React from 'react';
import "./Card.css"

interface CardParameters {
    cardIcon?: string;
    cardTitle?: string;
    cardBody?: string;
    cardLink?: string;
};

const Card: React.FC<CardParameters> = ({cardIcon, cardTitle, cardBody, cardLink}) => {
  return (
    <div className='w-[280px] h-[280px] /* Fixed height */ 
        rounded-2xl bg-white shadow-[0px_3px_3px_2px_gray]
        flex flex-col overflow-hidden hover:bg-green-100'> 
      
      {/* Icon Section (Fixed height) */}
      <div className='flex justify-center pt-6 pb-4'>
        <i className={`${cardIcon} text-5xl text-gray-500`}></i>
      </div>

      {/* Title Section (Fixed height) */}
      <div className='px-4'>
        <h6 className='text-2xl font-semibold text-gray-700 text-center'>
          {cardTitle}
        </h6>
      </div>

      {/* Body Section (Flexible with scroll) */}
      <div className='px-4 mt-3 flex-1 overflow-y-auto /* Scroll when needed */
          text-gray-400 text-lg text-center leading-6'>
        <p>{cardBody}</p>
      </div>

      {/* Link Section (Fixed height at bottom) */}
      {cardLink && (
        <div className='px-4 pb-4 pt-2'>
          <p className='text-blue-400 font-semibold text-sm text-center'>
            {cardLink}
            <i className="fas fa-chevron-right text-xs ml-1"></i>
          </p>
        </div>
      )}
    </div>
  )
}

export default Card;