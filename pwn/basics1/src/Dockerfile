#FROM alpine:3.15
FROM ubuntu:20.04
RUN mkdir chall && apt update -y && apt upgrade -y && apt install -y socat 
WORKDIR /chall
COPY flag.txt /chall/flag.txt
COPY chall /chall/

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork,su=root","EXEC:\"/chall/chall\""]
