#!/usr/bin/env bash

# Variables
PYTHON_VERSION=3.8.5
PG_VERSION=12
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
sudo apt-get install -y checkinstall \
libreadline-gplv2-dev \
libncursesw5-dev \
libssl-dev \
libsqlite3-dev \
python3-dev \
tk-dev \
libgdbm-dev \
libc6-dev \
libbz2-dev \
openssl \
libffi-dev \
python3-setuptools \
python3-pip \
zlib1g-dev \
python-pil \
libtiff5-dev \
libjpeg8-dev \
zlib1g-dev \
libfreetype6-dev \
liblcms2-dev \
libwebp-dev \
tcl8.6-dev \
tk8.6-dev \
python-tk


#
# Install Nginx
#
sudo apt-get install -y nginx
sudo cp /$PROJECT_NAME/deployment/nginx_conf /etc/nginx/sites-available/$PROJECT_NAME
sudo ln -s /etc/nginx/sites-available/$PROJECT_NAME /etc/nginx/sites-enabled/
sudo pip3 install uwsgi

#
# Setup Database
sudo apt-get install -y postgresql-contrib libpq-dev
sudo pip3 install psycopg2
sudo cp /$PROJECT_NAME/deployment/pg_hba.conf /etc/postgresql/$PG_VERSION/main/
sudo service postgresql restart
sudo createuser -U postgres -d vagrant
sudo createdb -U vagrant $PROJECT_NAME


#
# Install Python packages
#
# --ignore-installed is included because the Vagrant box includes binaries for several of our
# dependencies, but in the incorrect version. The existing installations are installed in such
# a way (using distutils) that pip can't upgrade them, so they have to be ignored.
#
sudo pip3 install --ignore-installed -r /$PROJECT_NAME/requirements.txt


#
# Install Node and NPM for React
#
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
cd /$PROJECT_NAME
sudo npm install -g watchify
sudo npm install
cd ..

#
# Populate local database
#
sudo createuser -U postgres -d hjgblmqzztzppf
sudo pg_restore -U hjgblmqzztzppf -d $PROJECT_NAME --clean /$PROJECT_NAME/deployment/initial_dataset_apr_11_2018
sudo psql -d $PROJECT_NAME -U postgres -c "REASSIGN OWNED BY hjgblmqzztzppf TO vagrant"


#
# Django migration: this isn't supposed to be automatized for now.
#
# python /farmview/manage.py makemigrations
# python /farmview/manage.py migrate

#
# Restart the server
#
sudo service postgresql restart
sudo service nginx restart

#
# Daemonize uWSGI module and start Watchify to bundle and transpile the JS
#
cd /$PROJECT_NAME
watchify src/pages/map-page.js -v --poll -t [ babelify ] -o static/src/pages/map-page.js > /var/log/watchify.log 2>&1 &

# cd /farmview && sudo uwsgi --daemonize /var/log/uwsgi-daemon.log --socket :8001 --module farmview.wsgi
sudo uwsgi --daemonize /var/log/uwsgi-daemon.log --socket :8001 --module $PROJECT_NAME.wsgi --touch-reload=/$PROJECT_NAME/reload.ini

# Otherwise, copy the command above to rc.local
# sudo cp /$PROJECT_NAME/deployment/uwsgi_daemon /etc/rc.local
