FROM cecton/nginx-with-substitution-filter
RUN apk update
RUN apk add python3
COPY my-default.conf /etc/nginx/conf.d/default.conf

