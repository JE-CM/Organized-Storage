import '@/app/ui/global.css';

import Footer from '@/app/lib/footer/footer.tsx';
import Header from '@/app/lib/header/header.tsx';

export default function LoginLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        {children}
        <Footer />
      </body>
    </html>
  );
}
