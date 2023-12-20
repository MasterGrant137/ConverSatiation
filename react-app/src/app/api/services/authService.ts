import jwt, { JwtPayload } from 'jsonwebtoken';
import { DEFAULT_JWT_SIGNATURE_OPTION, ResponseErrorsI } from '@/types/serviceTypes';
import { UserI } from '@/types/userTypes';

export const signJWT = (payload: JwtPayload, options = DEFAULT_JWT_SIGNATURE_OPTION): string => {
  const secretKey = process.env.JWT_SECRET_KEY as unknown as string;
  const token = jwt.sign(payload, secretKey, options);
  return token;
};

export const verifyJWT = (token: string): jwt.JwtPayload | string | null => {
  try {
    const secretKey = process.env.JWT_SECRET_KEY as unknown as string;
    const decoded = jwt.verify(token, secretKey);
    return decoded;
  } catch (error) {
    return null;
  }
};

export const loginService = async (
  email: string,
  password: string,
): Promise<UserI | ResponseErrorsI> => {
  const accessToken = signJWT({ email, password });

  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${accessToken}` },
    body: JSON.stringify({ email, password }),
  });

  const data: UserI | ResponseErrorsI = await response.json();
  return data;
};

// export const signupService = async (email: string, password: string): Promise<unknown> => {
//   const tempObj = { email, password };
//   return tempObj;
// };
