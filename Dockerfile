FROM python:3.10-slim

WORKDIR /work

COPY ./requirements.txt /work/
RUN pip install -r requirements.txt

COPY ./ris_6 /work/ris_6