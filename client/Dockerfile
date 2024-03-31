FROM node:20-alpine

WORKDIR /code

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm create vite@latest
RUN npm install --silent

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
