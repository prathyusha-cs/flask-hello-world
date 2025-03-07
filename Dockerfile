# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.9-slim
# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies (including Gunicorn)
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy and set permissions for the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]
