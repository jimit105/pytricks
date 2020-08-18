# Dockerfile for Python

Minimal Dockerfile for Python Applications

```dockerfile
FROM python:3.6

ENV PYTHONUNBUFFERED=0
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5010
CMD ["python", "-u", "./src/app.py"]
```
