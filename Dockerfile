FROM --platform=linux/arm64 python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application runs on
EXPOSE 8000

# Command to run the application
CMD ["/usr/local/bin/python", "app.py"]
