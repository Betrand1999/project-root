FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port Flask runs on
EXPOSE 50

# Start the application
CMD ["python", "app.py"]
