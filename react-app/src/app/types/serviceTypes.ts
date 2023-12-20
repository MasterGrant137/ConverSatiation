export interface ResponseErrorsI {
  errors: string[] | [];
}

export interface JWTSignatureOptionsI {
  expiresIn: string | number;
}

export const DEFAULT_JWT_SIGNATURE_OPTION: JWTSignatureOptionsI = {
  expiresIn: '1h',
} as const;
