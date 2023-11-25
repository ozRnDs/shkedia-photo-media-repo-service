FROM python:3.11.6

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY /src ./

ENTRYPOINT python3 main.py