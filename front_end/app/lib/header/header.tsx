"use client"

import React, { useState } from 'react';
import Image from 'next/image';


const Header: React.FC = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <header className="flex justify-between items-center bg-gray-800 text-white py-1 px-1 md:px-16 drop-shadow-md">
      {/* Logo */}

      <a href="/" >
        <Image src={'/assets/media/icons/logo.png'} alt='Logo'
          className='w-32 hover:scale-110 transition-all cursor-pointer'
          width={800}
          height={800} />
      </a>

      {/* Location */}
      <button className="p-4 bg-blue-500 text-white rounded-r transition-all cursor-pointer">
        location
      </button>

      {/* Search Bar */}
      <div className="flex-grow p-4 rounded-none focus:outline-none justify-center 
      gap-2 relative hidden md:flex items-center">

        <button
          onClick={toggleExpand}
          className="px-2 py-2 bg-gray-700 rounded hover:bg-gray-600"
        >
          All {isExpanded ? '△' : '▽'}
        </button>

        <input
          type="text"
          placeholder="Search here"
          className="py-0 w-3/5 p-2 text-lg rounded-l border-1 border-gray-300
          focus:bg-slate-100 focus:outline-sky-50"

        />
        <button className="p-1 px-2 py-2 bg-blue-500 text-white rounded-r">
          🔍
        </button>
      </div>

      {/* Navigation */}
      <nav className="flex-2 flex justify-end space-x-4">
        <a href="/" className="text-white hover:bg-gray-600 px-3 py-2 rounded">
          Home
        </a>
        <a href="/services" className="text-white hover:bg-gray-600 px-3 py-2 rounded">
          Services
        </a>
        <a href="/portfolio" className="text-white hover:bg-gray-600 px-3 py-2 rounded">
          Portfolio
        </a>
        <a href="/about" className="text-white hover:bg-gray-600 px-3 py-2 rounded">
          About Us
        </a>

        {/* Dark Mode Toggle */}
        <div className="relative">
          <button
            onClick={toggleExpand}
            className="px-3 py-2 bg-gray-700 rounded hover:bg-gray-600"
          >
            {isExpanded ? '🌙' : '☀'}
          </button>

        </div>
      </nav>
    </header>
  );
};

export default Header;
