
ARG APP_VERSION=1.0
FROM python:3.12-slim
LABEL maintainer="Prajwal B DevOps"
LABEL version=${APP_VERSION}
ENV APP_ENV=production
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home --shell /bin/bash flask-user && \
    chown -R flask-user:flask-user /app
USER flask-user
EXPOSE 5000
HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=10s \
            --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1
CMD ["python", "app.py"]
