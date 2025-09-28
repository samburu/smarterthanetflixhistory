# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expose Render's expected port
ENV PORT 10000
EXPOSE $PORT

# Start command
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:10000"]
