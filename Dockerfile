# Use the official Nginx image
FROM nginx:latest

# Copy your HTML and CSS files to the appropriate Nginx directory
COPY ./templates /usr/share/nginx/html
COPY ./static /usr/share/nginx/html/static

# Expose port 80 to allow web traffic
EXPOSE 80

# Nginx runs by default on port 80
CMD ["nginx", "-g", "daemon off;"]
