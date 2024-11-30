import React, { useState } from 'react';

const Footer: React.FC = () => {
  const [isExpanded, setIsExpanded] = useState(false);

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <footer className="bg-gray-100 p-5 text-center">
      {/* Navbar for expanding/collapsing additional information */}
      <div className="mb-4">
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

      {/* Informational Links */}
      <div className="mt-4 text-sm text-gray-700">
        <div className="flex justify-center flex-wrap gap-4 p-4 bg-gray-200">
          <a href="/work_with_Us" className="hover:underline">Work with Us</a>
          <a href="/terms_Conditions" className="hover:underline">Terms and Conditions</a>
          <a href="/promotions" className="hover:underline">Promotions</a>
          <a href="/privacy" className="hover:underline">About your privacy</a>
          <a href="/accessibility" className="hover:underline">Accessibility</a>

          {/* PQRSD / */}
          <a href="/help" className="hover:underline">Help, issues, claims, complaints</a>

          <a href="/discount" className="hover:underline">Discount</a>
          <a href="/hot_sale" className="hover:underline">Hot Sale</a>
          <a href="http://www.sic.gov.co" className="hover:underline">www.sic.gov.co</a>
        </div>

        {/*© Copyright and Address */}
        <p className="mt-4">&copy; 2024-20XX, Storage.com, Inc. or its affiliates</p>
        <p>Address: close location</p>
      </div>

      {/* Logos */}
      <div className="mt-6 flex justify-center gap-6">
        <img src="/assets/media/icons/logo.png" alt="Logo Ind" className="h-12" />
        <img src="/assets/media/icons/logo.png" alt="Logo Price" className="h-12" />
      </div>
    </footer>
  );
};

export default Footer;
