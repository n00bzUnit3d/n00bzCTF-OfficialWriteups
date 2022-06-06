FROM python:slim AS app

RUN pip install --no-cache-dir pycryptodome && apt update -y && \
    apt upgrade -y && apt install socat -y

WORKDIR /app/
COPY flag.txt /app/flag.txt
COPY hadispaide.py  /app/run

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,su=root","EXEC:\"/app/run\""]
