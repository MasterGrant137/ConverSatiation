FROM node:20 AS build-stage

WORKDIR /react-app
COPY react-app/. .

# Set REACT_APP_BASE_URL during build time
# ENV REACT_APP_BASR_URL=https://your-app-name.deployment-site.com/

# Build React app
RUN npm install
RUN npm run build

FROM python:3.11.3

# Set up Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

WORKDIR /var/www
COPY . .
COPY --from=build-stage /react-app/* app/static

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install psycopg2

# Run FLask environment
CMD gunicorn app:app
