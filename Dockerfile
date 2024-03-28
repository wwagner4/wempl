FROM cecton/nginx-with-substitution-filter
RUN apk update
RUN apk add python3
WORKDIR /app
COPY templates templates/
COPY entrypoint.py .
CMD ["python3", "entrypoint.py"]


