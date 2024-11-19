# syntax=docker/dockerfile:1

# Stage 1: Base image.

FROM node:lts as base

WORKDIR /app

# Stage : Development mode.
FROM base as dev

## Expose the port that Docusaurus will run on.
EXPOSE 3000

## Run the development server.
CMD [ -d "node_modules" ] && npm run start || npm install && npm run dev --host=0.0.0.0