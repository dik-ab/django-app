FROM python:3   
ENV PYTHONBUFFERED 1
RUN mkdir /echo
WORKDIR /echo
COPY requirements.txt /echo/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /echo/