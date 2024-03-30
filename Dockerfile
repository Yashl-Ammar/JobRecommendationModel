# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your Flask app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
