"use client"

import Footer from '@/app/ui_ux/components/footer/footer';
import Header from '@/app/ui_ux/components/header/header';

export default function LoginLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      {children}
    </>
  );
}
