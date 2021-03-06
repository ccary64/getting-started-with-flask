FROM alpine:3.8

RUN apk add --no-cache python3 gcc musl-dev sqlite python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    m -r /root/.cache

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app