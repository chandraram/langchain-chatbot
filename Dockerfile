# # Use an official Python image
# #rampucsd15 1415@#$Pandu #
# #rampucsd15 1415@#$Pandu #B5690EEEBB952194
# FROM python:3.11-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy dependency list and install
# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the FastAPI application code
# COPY . .

# # Expose the port FastAPI will run on
# EXPOSE 8000

# # Command to run the FastAPI app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Use an official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
