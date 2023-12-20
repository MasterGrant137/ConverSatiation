export interface UserAuthI {
  username: string;
  email: string;
}

export interface UserI extends UserAuthI {
  id: number;
}
