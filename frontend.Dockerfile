FROM node:21.5.0-alpine3.18

WORKDIR /react-app

VOLUME /react-app

COPY ./react-app/tsconfig.json /react-app/tsconfig.json

COPY ./react-app/package.json /react-app/package.json

RUN npm install

CMD ["npm", "run", "dev"]
