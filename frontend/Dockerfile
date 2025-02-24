FROM node:23.8.0-alpine3.21 AS builder

WORKDIR /code

COPY package*.json ./
RUN npm install
COPY . ./

ARG PUBLIC_API_HOST
ARG PUBLIC_API_PORT
ENV PUBLIC_API_HOST $PUBLIC_API_HOST
ENV PUBLIC_API_PORT $PUBLIC_API_PORT
RUN npm run build && \
    npm prune --production


FROM node:23.8.0-alpine3.21

WORKDIR /code

COPY --from=builder /code/build ./build
COPY --from=builder /code/package.json ./

ENV NODE_ENV=production

CMD ["node", "build"]