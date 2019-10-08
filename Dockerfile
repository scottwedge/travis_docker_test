FROM alpine:latest

RUN apk add bash python3\
  && mkdir /work
WORKDIR /work
COPY *.py  /work/
RUN chmod +x test_script.py
CMD bash "/work/test_script.py"
