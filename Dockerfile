# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages (SQLite is built-in to Python)
RUN pip install --no-cache-dir --upgrade pip

# Create data directory if it doesn't exist
RUN mkdir -p data

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Default command to run
CMD ["python3", "lab.py", "status"]
