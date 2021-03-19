FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# add and run as non-root user
# RUN adduser -D myuser
# USER myuser

#CMD python manage.py runserver 0.0.0.0:8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT

