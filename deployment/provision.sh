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
sudo apt-get install -y python-pip
sudo apt-get install -y python-dev # Required for compilation of Python extensions written in C or C++, like psycopg2
PYTHON_VERSION=2.7.13
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.13/Python-$PYTHON_VERSION.tgz
sudo tar xzf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION
sudo ./configure
sudo make install
sudo pip install --upgrade pip
sudo pip install virtualenv
cd /farmview
virtualenv -p /usr/local/bin/python venv
source venv/bin/activate
# sudo apt-get install -y python-virtualenv
# http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
# Deploying static files


# 
# Install Nginx
# 
sudo apt-get install -y nginx
sudo cp /farmview/deployment/nginx_conf /etc/nginx/sites-available/farmview
sudo ln -s /etc/nginx/sites-available/farmview /etc/nginx/sites-enabled/
sudo pip install uwsgi
# uwsgi --http :8888 --module farmview.wsgi --virtualenv /farmview/venv


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

deactivate
