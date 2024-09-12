FROM node:18-alpine AS build
WORKDIR /app
RUN npm install -g @angular/cli
COPY ./package.json .
RUN npm install
COPY . .
RUN ng build

# Serve Application using Nginx Server
FROM nginx:alpine
COPY ./nginx.conf /etc/nginx/conf.d/default.conf 
COPY --from=build /app/dist/org-prj-ui/ /usr/share/nginx/html
