# Stage 1 - Build the Flask app
FROM python:3.10 AS flask-build

WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask port (default Flask port 5000)
EXPOSE 5000

# Stage 2 - Build Nginx
FROM nginx:latest

# Remove the following line since you don't need custom nginx.conf
# COPY nginx.conf /etc/nginx/nginx.conf

# Copy static and templates folders to Nginx directory
COPY ./static /usr/share/nginx/html/static
COPY ./templates /usr/share/nginx/html

# Copy Flask app from the previous build stage
COPY --from=flask-build /app /app

# Expose port 80 for Nginx
EXPOSE 80

# Set environment variables for AWS (only for demo; not secure for production)
ENV AWS_ACCESS_KEY_ID=your-access-key
ENV AWS_SECRET_ACCESS_KEY=your-secret-key

# Install Supervisor to manage processes
RUN apt-get update && apt-get install -y supervisor

# Copy supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Command to run Supervisor, which starts Nginx and Flask
CMD ["supervisord", "-n"]
