FROM python:3.11-slim

WORKDIR /app

ENV FLASK_ENV=production

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["waitress-serve", "--listen=0.0.0.0:8000", "airport_near:app"]