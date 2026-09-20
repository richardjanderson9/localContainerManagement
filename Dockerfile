# Use a slim, official Python image for a smaller footprint
FROM python:3.11-slim

# Prevent Python from writing pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user and group for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY app.py .

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Run the Python script
CMD ["python", "app.py"]