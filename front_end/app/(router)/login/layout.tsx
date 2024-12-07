"use client"

import Footer from '@/app/lib/header/header.tsx';
import Header from '@/app/lib/footer/footer.tsx';


export default function LoginLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <Header />
      {children}
      <Footer />
    </>
  );
}
