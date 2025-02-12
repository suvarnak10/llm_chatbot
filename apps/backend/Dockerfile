# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy only requirements.txt first to leverage caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

# Expose FastAPI port
EXPOSE 8000

# Keep container running
CMD ["tail", "-f", "/dev/null"]

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]