FROM python:slim

RUN apt update -y && \
    apt upgrade -y && apt install socat -y

WORKDIR /app
COPY jail.py secret /app/

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,su=root","EXEC:\"/app/jail.py\""]
