# Use the official Python image as a base image
FROM python:latest

WORKDIR /merocv/

COPY requirements.txt /merocv/

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . /merocv/

# Run database migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "merocv.wsgi:application", "--bind", "0.0.0.0:8000"]
