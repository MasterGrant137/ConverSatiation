import { createContext, useMemo, useState } from 'react';
import { loginService } from '@/api/services/authService';
import { ResponseErrorsI } from '@/types/serviceTypes';
import { UserI } from '@/types/userTypes';

interface AuthContextI {
  authErrors: ResponseErrorsI;
  login: (email: string, password: string) => Promise<void>;
  user: UserI | null;
}

const authContextDefaultValues = {
  authErrors: [] as unknown as ResponseErrorsI,
  login: async (): Promise<void> => { },
  user: null,
};

export const AuthContext = createContext<AuthContextI>(authContextDefaultValues);

export default function AuthContextProvider({ children }: {
  children: React.ReactNode
}): JSX.Element {
  const [user, setUser] = useState<UserI | null>(null);
  const [authErrors, setAuthErrors] = useState<ResponseErrorsI>([] as unknown as ResponseErrorsI);

  const login = async (email: string, password: string): Promise<void> => {
    const data = await loginService(email, password);

    if ('errors' in data) setAuthErrors(data);
    else setUser(data);
  };

  const value = useMemo(() => ({
    authErrors,
    login,
    user,
  }), [authErrors, user]);

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}
