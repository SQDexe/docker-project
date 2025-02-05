FROM node:23.7.0

WORKDIR /code

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . ./
RUN npm run build

CMD ["node", "build"]