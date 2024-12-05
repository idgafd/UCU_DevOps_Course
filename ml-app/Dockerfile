# Stage 1: Build
FROM python:3.9-slim AS build

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and static files
COPY app.py .
COPY static ./static

# Stage 2: Final Image
FROM python:3.9-slim

WORKDIR /app

# Copy dependencies from the build stage
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copy the application and static files
COPY app.py .
COPY static ./static

# Use a non-root user
RUN groupadd -r webservice && useradd --no-log-init -r -g webservice webservice
USER webservice:webservice

EXPOSE 8050
ENTRYPOINT ["python", "app.py"]
