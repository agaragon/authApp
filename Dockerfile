# Use the official Python image as the base
FROM python:3.9

# Copy the requirements file
COPY requirements.txt .

# Install the required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app /app

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the entry point command to run the application
CMD ["python", "/app/main.py"]
