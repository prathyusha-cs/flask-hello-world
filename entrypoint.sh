#!/bin/sh
echo "Running database migrations..."
flask db upgrade

echo "Starting the application..."
exec gunicorn -b 0.0.0.0:5000 app:app