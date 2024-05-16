#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update package lists
sudo apt-get update

# Install Nginx web server
sudo apt-get -y install nginx

# Allow HTTP for Nginx
sudo ufw allow 'Nginx HTTP'

# Create Directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change owners
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration file
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx Server
sudo service nginx restart
