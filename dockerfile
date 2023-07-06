FROM python:3.9.5-slim
# FROM python:latest
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --user -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000
