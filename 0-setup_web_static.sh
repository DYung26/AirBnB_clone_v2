#!/usr/bin/env bash
# sets up web servers for the deployment of `web_static`.

sudo apt-get update -y
sudo apt-get install nginx -y
# sudo mkdir -p /data/
# sudo mkdir -p /data/web_static/
# sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello DYung!" | sudo tee /data/web_static/releases/test/index.html > /dev/null

if [ ! -L "/data/web_static/current" ]; then
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/^\t*server_name _;/a\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/hbnb_static\/;\n\t\tindex index.html;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
