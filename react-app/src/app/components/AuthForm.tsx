'use client';

import { Button, Stack } from '@mui/material';
import TextField from '@mui/material/TextField';
import Grid2 from '@mui/material/Unstable_Grid2/Grid2';
import { ChangeEvent, useContext, useState } from 'react';
import { AuthContext } from '@/context/AuthContext';

interface AuthFormProps {
  AuthType: 'Login' | 'Signup',
}

export default function AuthForm({ AuthType }: AuthFormProps): JSX.Element {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useContext(AuthContext);

  const loginFormSubmitHandler = async (): Promise<void> => {
    await login(email, password);
  };

  const emailChangeHandler = (
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ): void => {
    setEmail(event.target.value);
  };

  const passwordChangeHandler = (
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ): void => {
    setPassword(event.target.value);
  };

  return (
    <Grid2 container height="100vh" alignContent="center" justifyContent="center">
      <Grid2>
        <Stack>
          {AuthType === 'Signup' && (<TextField label="Username" variant="standard" />)}
          <TextField label="Email" onChange={emailChangeHandler} type="email" value={email} variant="standard" />
          <TextField label="Password" onChange={passwordChangeHandler} type="password" value={password} variant="standard" />
          <Button onClick={loginFormSubmitHandler} variant="text">Submit</Button>
        </Stack>
      </Grid2>
    </Grid2>
  );
}
