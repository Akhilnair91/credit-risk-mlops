# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy only the requirements file first (Docker caching optimization)
COPY requirements.txt /app/requirements.txt

# Install dependencies first (Docker will cache this step)
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application files
COPY . /app

# Ensure the models directory is copied
COPY models /app/models

# Expose port 8081 for API
EXPOSE 8081

# Command to run FastAPI application
CMD ["uvicorn", "deployment.deploy_api:app", "--host", "0.0.0.0", "--port", "8081"]
