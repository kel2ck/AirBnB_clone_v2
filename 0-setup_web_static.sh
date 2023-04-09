#!/usr/bin/env bash
# Set up web servers for the deployment of web static

sudo apt-get update
sudo apt-get -y install nginx

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a test HTML file in the required directory
sudo tee /data/web_static/releases/test/index.html >/dev/null <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
#Create a symbolic link in current linked to test
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
# Make the user and group ubuntu the owner of the file
sudo chown -R ubuntu:ubuntu /data/
# Edit the default file to make /hbnb_static point to a directory
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# Restart Nginx
sudo service nginx restart
