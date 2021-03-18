FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#COPY . .
#ADD . /usr/src/app

#RUN python manage.py runserver
#CMD [ "python", "./manage.py runserver" ]
#CMD python manage.py runserver 0.0.0.0:8000
