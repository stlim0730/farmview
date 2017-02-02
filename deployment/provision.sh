#!/usr/bin/env bash


# 
# Create a symbolic link to the working directory
# 
ln -s /vagrant /farmview


# 
# Keep package list information up to date
# 
sudo apt-get update


# 
# Utilities
# 
sudo apt-get install -y git


# 
# Setup Python
# 
PYTHON_VERSION=2.7.13
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.13/Python-$PYTHON_VERSION.tgz
sudo tar xzf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION
sudo ./configure
sudo make install
cd /usr/src
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
# sudo apt-get install -y python-pip
# sudo apt-get install -y python-dev # Required for compilation of Python extensions written in C or C++, like psycopg2
# sudo pip install --upgrade pip
# sudo apt-get install -y python-virtualenv


# 
# Install Nginx
# 
sudo apt-get install -y nginx
cp /farmview/deployment/nginx_conf /etc/nginx/sites-available/farmview
ln -s /etc/nginx/sites-available/farmview /etc/nginx/sites-enabled/
sudo pip install uwsgi


# 
# Setup Database
# 
PG_VERSION=9.3
sudo apt-get install -y postgresql-$PG_VERSION
sudo apt-get install -y postgresql-contrib
sudo apt-get install -y libpq-dev # required for psycopg2
sudo apt-get install -y python-psycopg2
sudo cp /farmview/deployment/pg_hba.conf /etc/postgresql/$PG_VERSION/main/
sudo service postgresql restart
sudo createuser -U postgres -d vagrant
sudo createdb -U vagrant farmview
# pip install psycopg2 # installed using os package apt-get


# 
# Install Python packages
# 
sudo pip install -r /farmview/requirements.txt


# 
# Restart the server
# 
sudo service postgresql restart
sudo service nginx restart
