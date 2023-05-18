FROM nginx:1.19.0-alpine
EXPOSE 8080
RUN rm -r /etc/nginx/conf.d/*
COPY ./nginx.conf /etc/nginx/
COPY ./conf.d/ /etc/nginx/conf.d/