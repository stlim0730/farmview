#!/usr/bin/env bash

# Variables
# PYTHON_VERSION=2.7.13 # Currently, this project uses the native version of Python on the OS
PG_VERSION=9.3
PROJECT_NAME=farmview


# 
# Create a symbolic link to the working directory
# 
ln -s /vagrant /$PROJECT_NAME


# 
# Keep package list information up to date
# 
sudo apt-get update


# 
# Utilities
# 
sudo apt-get install -y build-essential # Required for building ANYTHING on ubuntu
sudo apt-get install -y git


# 
# Setup Python
# 
# sudo apt-get install -y python-pip
sudo apt-get install -y python-dev python-setuptools python-imaging libssl-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo easy_install pip
# Setup newer version of Python: Currently, this project uses the native version of Python on the OS
# cd /usr/src
# sudo wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
# sudo tar xzf Python-$PYTHON_VERSION.tgz
# cd Python-$PYTHON_VERSION
# sudo ./configure
# sudo make install
# export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH
# sudo pip install --upgrade pip

# sudo apt-get install -y python-virtualenv


# 
# Install Nginx
# 
sudo apt-get install -y nginx
cp /$PROJECT_NAME/deployment/nginx_conf /etc/nginx/sites-available/$PROJECT_NAME
ln -s /etc/nginx/sites-available/$PROJECT_NAME /etc/nginx/sites-enabled/
sudo pip install uwsgi


# 
# Setup Database
# 
sudo apt-get install -y postgresql-$PG_VERSION
sudo apt-get install -y postgresql-contrib
sudo apt-get install -y libpq-dev # required for psycopg2
sudo apt-get install -y python-psycopg2
sudo cp /$PROJECT_NAME/deployment/pg_hba.conf /etc/postgresql/$PG_VERSION/main/
sudo service postgresql restart
sudo createuser -U postgres -d vagrant
sudo createdb -U vagrant $PROJECT_NAME


# 
# Install Python packages
# 
# sudo pip install -r /$PROJECT_NAME/requirements.txt


# 
# Restart the server
# 
sudo service postgresql restart
sudo service nginx restart
