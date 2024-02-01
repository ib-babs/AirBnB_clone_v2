#!/usr/bin/env bash
# Server configuration: Automating script for the server

if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get install nginx -y
fi

if ! [ -e '/data/web_static/shared/' ]; then
    sudo mkdir -p /data/web_static/shared/
fi
if ! [ -e '/data/web_static/releases/test/' ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

# Creating html file
if ! [ -e '/data/web_static/releases/test/index.html' ]; then
    echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html >/dev/null 2>&1

fi

# Creating a symlink to /data/web_static/releases/test/ dir
if [ -L '/data/web_static/current' ]; then
    sudo rm -rf /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

# Nginx configuration
nginx_config="\
server{
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}
"
echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default >/dev/null 2>&1

sudo service nginx restart
