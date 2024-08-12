
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    git \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

CMD ["/bin/sh"]
