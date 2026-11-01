# Small, official base image
FROM python:3.12-slim

# Don't write .pyc files; flush logs immediately (so `kubectl logs` shows them)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first -> Docker caches this layer if code changes but deps don't
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Run as a non-root user (security best practice)
RUN useradd --create-home appuser
USER appuser

EXPOSE 5000

# Production-grade WSGI server instead of Flask's dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "app:app"]
