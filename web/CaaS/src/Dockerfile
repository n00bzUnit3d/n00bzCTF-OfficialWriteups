FROM python:slim

RUN mkdir -p /chall && mkdir -p /chall/templates && pip3 install flask
WORKDIR /chall

COPY challenge.py /chall
COPY templates /chall/templates

EXPOSE 8000
ENTRYPOINT ["python", "challenge.py"]
