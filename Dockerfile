# Use the official Python image as a base image
FROM python:latest

WORKDIR /merocv/

COPY requirements.txt /merocv/

RUN pip install -r requirements.txt

COPY app/ /merocv/app/

EXPOSE 8000

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
