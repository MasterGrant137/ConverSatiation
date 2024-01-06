'use client';

import AuthContextProvider from '@/context/AuthContext';

export default function Providers({ children }: { children: React.ReactNode }): JSX.Element {
  return (
    <AuthContextProvider>
      {children}
    </AuthContextProvider>
  );
}
