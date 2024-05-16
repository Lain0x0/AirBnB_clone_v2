#!/usr/bin/env bash
# Set up a web server {NGINX} for the deployement of {web_static}

# Updating the system and Installing the web server
sudo apt -y update
sudo apt -y install nginx

# Allowing HTTP for Nginx
sudo ufw allow "Nginx HTTP"

# Making Directories
sudo mkdir -p /data/ 
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creating a fake HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Alx Foundation
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating a symbolik link to another path
sudo ln -s -f /data/web_static/current /data/web_static/releases/test/

# Giving Access
sudo chown -R "$USER":"$USER" /data/

# Updating the Nginx web server configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restarting the server
sudo service nginx restart

