FROM python:3.12-slim as base

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

FROM base as dev

EXPOSE 8000

CMD sh -c "pip install --no-cache-dir -r /app/requirements.txt && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
