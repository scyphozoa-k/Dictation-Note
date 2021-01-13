FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /dictation-note
WORKDIR /dictation-note
COPY requirements.txt /dictation-note/
RUN pip install -r requirements.txt
COPY . /dictation-note/