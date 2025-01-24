# Python
FROM python:3.11-slim

# Install PostgreSQL development files and dependencies for building psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Set up working directory
WORKDIR /app

# Copy requirements file first to improve Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache -r requirements.txt

# Copy the code
COPY . .

# Command to run the python app
CMD ["python", "homework_29.py"]
