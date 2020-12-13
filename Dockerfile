FROM alpine:3.7

RUN apk add --no-cache python3 \
                       python3-dev \
                       make

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --upgrade pip==20.3.1 && \
    pip3 install -r requirements.txt

COPY . .
