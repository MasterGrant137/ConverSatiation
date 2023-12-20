import { NextRequest, NextResponse } from 'next/server';

const unprotectedRoutes: string[] = ['/login', '/signup'];

export default function middleware(request: NextRequest): NextResponse<unknown> | null {
  if (!unprotectedRoutes.includes(request.nextUrl.pathname)) {
    const absoluteURL = new URL('/login', request.nextUrl.origin);
    return NextResponse.redirect(absoluteURL.toString());
  }
  return null;
}

export const config = {
  matcher: ['/'],
};
