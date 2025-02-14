# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /backend

# Copy only requirements.txt first to leverage caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Keep container running
CMD ["tail", "-f", "/dev/null"]

# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]