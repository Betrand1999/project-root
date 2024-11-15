# Stage 1 - Build the Flask app
FROM python:3.10 AS flask-build

WORKDIR /app

# Copy the application code into the container
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port (default Flask port 5000)
EXPOSE 5000

# Stage 2 - Set up Nginx to serve static files and proxy to Flask app
FROM nginx:latest

# Remove the default Nginx configuration to ensure no conflicts
RUN rm /etc/nginx/conf.d/default.conf

# Copy the static files and templates to Nginx directory
COPY ./static /usr/share/nginx/html/static
COPY ./templates /usr/share/nginx/html/templates

# Copy Flask app from the first build stage into the Nginx container
COPY --from=flask-build /app /app

# Expose Nginx port 80
EXPOSE 80

# Install Supervisor to manage both Flask and Nginx
RUN apt-get update && apt-get install -y supervisor

# Copy Supervisor configuration to the container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Command to run Supervisor, which starts both Nginx and Flask
CMD ["supervisord", "-n"]
