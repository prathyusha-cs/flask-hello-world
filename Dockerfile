# Use the official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY .. .

# Expose the port the app runs on
EXPOSE 5000

# Run the application

CMD ["python", "app.py"]
