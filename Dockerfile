# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir pygame

# Copy your Python scripts into the Docker image
COPY bfs.py /app/
COPY matrix.py /app/
COPY main.py /app/

# Run your main script when the container starts
CMD ["python", "main.py"]
