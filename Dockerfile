FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install dependencies and package
RUN pip install --no-cache-dir -e .

# Expose standard Cloud Run port
ENV PORT=8080
EXPOSE 8080

# Run lightweight health check service or verification runner
CMD ["python3", "-m", "strix_duo.server"]
