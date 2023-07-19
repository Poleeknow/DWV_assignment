FROM python:3.10-bookworm

COPY . . 

RUN pip install -r requirements.txt
EXPOSE 9999
RUN python3 server.py

