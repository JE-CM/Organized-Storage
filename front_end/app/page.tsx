'use client'

import React, { useState, useEffect, useRef } from 'react';

const Footer: React.FC = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  const images = [
    { src: 'small_storage.png', alt: 'Small Storage', caption: 'Small Storage', link: 'small_storage.html' },
    { src: 'medium_storage.png', alt: 'Medium Storage', caption: 'Medium Storage', link: 'medium_storage.html' },
    { src: 'large_storage.png', alt: 'Large Storage', caption: 'Large Storage', link: 'large_storage.html' },
  ];

  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [animation, setAnimation] = useState('');

  const nextImage = () => {
    const newIndex = (currentImageIndex + 1) % images.length;
    setAnimation('slide-out-left');
    setTimeout(() => {
      setCurrentImageIndex(newIndex);
      setAnimation('slide-in-right');
    }, 500);
  };

  const prevImage = () => {
    const newIndex = (currentImageIndex - 1 + images.length) % images.length;
    setAnimation('slide-out-right');
    setTimeout(() => {
      setCurrentImageIndex(newIndex);
      setAnimation('slide-in-left');
    }, 500);
  };

  const goToPage = (link: string) => {
    window.location.href = link;
  };

  const contentRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const content = contentRef.current;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-fadeInSlideIn');
          }
        });
      },
      { threshold: 0.1 }
    );

    if (content) {
      observer.observe(content);
    }

    return () => {
      if (content) observer.unobserve(content);
    };
  }, []);

  return (
    <footer className="bg-gray-100 p-5 text-center">
{/* Logo */}

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
        
      <div className="flex justify-center items-center p-5 bg-gray-300/80 z-1000">
      <div className="text-xl font-bold">storage
      <nav className="flex space-x-6">
        <a href="#about" className="text-black font-bold hover:underline">
          About us
        </a>
        <a href="#" className="text-black font-bold hover:underline">
          Services
        </a>
        <a href="#types_of_storage" className="text-black font-bold hover:underline">
          Storage
        </a>
        <a href="#" className="text-black font-bold hover:underline">
          Cart
        </a>
        <a href="#" className="text-black font-bold hover:underline">
          Log in
        </a>
      </nav>
      </div>
      </div>

      <div className="flex flex-col items-center space-y-10">
      {/* Main Content Section */}
      <div className="text-center p-12 bg-gray-300/80 w-4/5 rounded-lg shadow-lg animate-fadeIn">
        <h1 className="text-3xl font-bold mb-5 animate-slideIn">
          The Best Storage Unit Solution
        </h1>
        <div className="space-x-4">
          <button className="px-5 py-2 bg-orange-500 text-white font-bold rounded hover:bg-orange-400 transition duration-300">
            Rent Storage
          </button>
          <button className="px-5 py-2 bg-orange-500 text-white font-bold rounded hover:bg-orange-400 transition duration-300">
            Offer Storage
          </button>
        </div>
      </div>

      {/* Search Section */}
      <div className="text-center p-8 bg-gray-200/80 w-4/5 rounded-lg shadow-lg border-t border-gray-300 animate-fadeIn">
        <h2 className="text-2xl font-semibold mb-5 animate-slideIn">
          Find the Nearest Storage Facility
        </h2>
        <div className="space-y-4">
          <input
            type="text"
            placeholder="Location"
            className="w-52 p-2 rounded border border-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
          <input
            type="text"
            placeholder="Unit Size (Optional)"
            className="w-52 p-2 rounded border border-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
          <input
            type="text"
            placeholder="Type (Optional)"
            className="w-52 p-2 rounded border border-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
          <input
            type="text"
            placeholder="Date (Optional)"
            className="w-52 p-2 rounded border border-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-400"
          />
        </div>
        <button className="mt-5 px-5 py-2 bg-orange-500 text-white font-bold rounded hover:bg-orange-400 transition duration-300">
          Find Storage
        </button>
      </div>
    </div>

    <div
      id="about"
      className="flex flex-col md:flex-row items-center gap-12 max-w-4xl p-5 bg-white shadow-lg rounded-lg mx-auto"
    >
      {/* Text Section */}
      <div className="max-w-xs text-center md:text-left">
        <h1 className="text-2xl font-bold mb-5">About Us</h1>
        <p className="text-base leading-relaxed text-gray-800">
          [Facility Name] is your trusted partner for convenient and affordable self-storage solutions. We offer a variety
          of storage unit sizes to accommodate your needs, whether you're moving, downsizing, or simply need extra space.
        </p>
      </div>

      {/* Image Section */}
      <div className="flex justify-center items-center w-[450px] h-[450px] bg-gray-300 rounded-lg">
        <img
          src="about_us.png"
          alt="Image placeholder"
          className="w-[90%] h-[90%] rounded-lg object-cover"
        />
      </div>
    </div>

    <div
      id="types_of_storage"
      className="text-center w-[600px] mx-auto p-6 bg-gradient-to-br from-gray-100 to-gray-200 rounded-xl shadow-lg border border-gray-300"
    >
      <h2 className="text-2xl font-bold mb-4">Types of Storage</h2>
      <div className="relative w-full h-[500px] bg-gray-300 rounded-lg overflow-hidden flex justify-center items-center border border-black">
        {/* Left Arrow */}
        <span
          className="absolute left-4 top-1/2 transform -translate-y-1/2 text-2xl bg-white/80 p-2 cursor-pointer rounded-md shadow-md z-10"
          onClick={prevImage}
        >
          &#9664;
        </span>

        {/* Images */}
        {images.map((image, index) => (
          <img
            key={index}
            src={image.src}
            alt={image.alt}
            className={`absolute w-auto h-auto max-w-full max-h-full rounded-lg border-4 border-white transition-opacity duration-500 ${
              index === currentImageIndex
                ? `opacity-100 ${animation}`
                : 'opacity-0'
            }`}
            onClick={() => goToPage(image.link)}
          />
        ))}

        {/* Right Arrow */}
        <span
          className="absolute right-4 top-1/2 transform -translate-y-1/2 text-2xl bg-white/80 p-2 cursor-pointer rounded-md shadow-md z-10"
          onClick={nextImage}
        >
          &#9654;
        </span>
      </div>
      <p className="mt-4 text-lg">{images[currentImageIndex].caption}</p>
    </div>


    <div>
      {/* Payment Options Section */}
      <div className="flex justify-center items-center mt-10 p-5">
        <div className="flex items-center justify-center bg-white p-10 rounded-lg shadow-lg">
          {/* Payment Text Section */}
          <div className="text-2xl font-bold text-gray-800 mr-10">
            Payment Options
          </div>

          {/* Payment Image Section */}
          <div className="flex gap-5">
            <img
              src="visa.jpg"
              alt="Visa"
              className="w-20 h-20 rounded-lg opacity-80 transition-transform duration-300 hover:scale-110 hover:opacity-100 animate-bounce"
            />
            <img
              src="mastercard.png"
              alt="Mastercard"
              className="w-20 h-20 rounded-lg opacity-80 transition-transform duration-300 hover:scale-110 hover:opacity-100 animate-bounce"
            />
            <img
              src="dollar_sign.png"
              alt="Dollar Sign"
              className="w-20 h-20 rounded-lg opacity-80 transition-transform duration-300 hover:scale-110 hover:opacity-100 animate-bounce"
            />
          </div>
        </div>
      </div>

      {/* What Size Do I Need Section */}
      <div className="flex max-w-4xl w-4/5 mx-auto bg-white rounded-lg shadow-xl mt-10 overflow-hidden transform transition duration-300 hover:scale-105">
        {/* Size Guide Image Section */}
        <div className="flex-1 flex items-center justify-center">
          <img
            src="what_size_do_i_need.png"
            alt="Size Guide Image"
            className="w-full h-auto object-cover"
          />
        </div>

        {/* Size Guide Text Section */}
        <div className="flex-1 flex flex-col justify-center items-center p-5 text-center bg-gray-800 text-white">
          <h1 className="text-3xl mb-5">What Size Do I Need?</h1>
          <button className="px-6 py-3 bg-blue-400 rounded-full text-gray-800 text-lg font-semibold hover:bg-blue-500 transform transition duration-300 hover:translate-y-[-3px]">
            Find Out
          </button>
        </div>
      </div>
    </div>

      {/* Navbar for expanding/collapsing additional information */}
      <div className="mt-8 mb-4">
        <button
          onClick={toggleExpand}
          className="bg-transparent border-none text-blue-500 cursor-pointer text-lg"
        >
          {isExpanded ? '- Information ▼' : '+ Information ▲'}
        </button>

        {isExpanded && (
          <nav className="mt-2 flex justify-center flex-wrap gap-4 text-sm">
            {/* Additional expandable links can go here */}
          </nav>
        )}
      </div>

      <div ref={contentRef} className="opacity-0">
      {/* Informational Links */}
      <div className="mt-4 text-sm text-gray-700">
        <div className="flex justify-center flex-wrap gap-4 p-4 bg-gray-200">
          <a href="/work_with_Us" className="hover:underline">
            Work with Us
          </a>
          <a href="/terms_Conditions" className="hover:underline">
            Terms and Conditions
          </a>
          <a href="/promotions" className="hover:underline">
            Promotions
          </a>
          <a href="/privacy" className="hover:underline">
            About your privacy
          </a>
          <a href="/accessibility" className="hover:underline">
            Accessibility
          </a>
          <a href="/help" className="hover:underline">
            Help, issues, claims, complaints
          </a>
          <a href="/discount" className="hover:underline">
            Discount
          </a>
          <a href="/hot_sale" className="hover:underline">
            Hot Sale
          </a>
          <a href="http://www.sic.gov.co" className="hover:underline">
            www.sic.gov.co
          </a>
        </div>
        <p className="mt-4">&copy; 2024-20XX, Storage.com, Inc. or its affiliates</p>
        <p>Address: close location</p>
      </div>
      {/* Logos */}
      <div className="mt-6 flex justify-center gap-6">
        <img
          src="/assets/media/icons/logo.png"
          alt="Logo Ind"
          className="h-12"
        />
        <img
          src="/assets/media/icons/logo.png"
          alt="Logo Price"
          className="h-12"
        />
      </div>
    </div>
  </footer>
  );
};

export default Footer;
