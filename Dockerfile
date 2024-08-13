
FROM python:3.10-slim

RUN adduser --disabled-password --shell /bin/sh newuser

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ishikki-akabane/sample .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R newuser:newuser /app
        
USER newuser

CMD "python3 bot.py"
