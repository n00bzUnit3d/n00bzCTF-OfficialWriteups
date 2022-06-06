FROM python:slim AS app

RUN pip install --no-cache-dir pycryptodome

FROM pwn.red/jail
COPY --from=app / /srv

COPY flag.txt /srv/app/flag.txt
COPY rsaoops.py /srv/app/run

ENV JAIL_TIME 1200
ENV JAIL_MEM=20M