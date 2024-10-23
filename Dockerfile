# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Set environment variables if needed (e.g., to suppress Python's .pyc files)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose any ports the application might need (change if necessary)
EXPOSE 8000

# Command to run the application (adjust as needed, depending on the project entry point)
CMD ["python", "slides_to_video.py"]