#!/usr/bin/env bash
# Set up web servers for the deployment of web static
# Install Nginx if it's not installed
if ! [ -x "$(command -v nginx)" ]; then
    echo "Nginx not installed. Installing..."
    sudo apt-get update
    sudo apt-get -y install nginx
else
    echo "Nginx already installed"
fi
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
# Create a temporary file containing the configuration block
cat <<'EOF' > /tmp/temp_block
        location /hbnb_static/ {
            alias /data/web_static/current/;
        }
EOF
# Insert the contents of the temporary file after the 10th line
sudo sed -i '10r /tmp/temp_block' /etc/nginx/sites-available/default
# Remove the temporary file
rm /tmp/temp_block
# Restart Nginx
sudo service nginx restart
