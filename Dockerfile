FROM cecton/nginx-with-substitution-filter
RUN apk update
RUN apk add python3
WORKDIR /app
COPY wempl-default.conf .
COPY create_subs:filter.py .


