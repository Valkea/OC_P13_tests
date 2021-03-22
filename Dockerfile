FROM python:3.8

# sets the environment variable
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBUG=1 \
    PORT=8000 \
    SENTRY_DSN=https://11111111111111111111111111111111@o555555.ingest.sentry.io/5555555

EXPOSE 8000

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# add and run as non-root user
# RUN adduser -D myuser
# USER myuser

RUN python manage.py collectstatic --noinput --clear

#CMD python manage.py runserver 0.0.0.0:8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT

