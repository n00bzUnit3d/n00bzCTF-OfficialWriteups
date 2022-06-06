FROM python:slim AS app

RUN pip install --no-cache-dir pycryptodome && apt update -y && \
    apt upgrade -y && apt install socat -y

# changed to make hosting easier
# even though redpwn jail image is more secure, it requires more
# work to have a script to host the chall
# so using normal image only
# maybe next time a more secure image
# FROM pwn.red/jail
# COPY --from=app / /srv

WORKDIR /app/
COPY flag.txt /app/flag.txt
COPY rsaoops.py /app/run

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,su=root","EXEC:\"/app/run\""]
