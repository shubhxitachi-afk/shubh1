FROM python:3.10-slim

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc g++ git ca-certificates && \
    update-ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD bash start
