# Farmview

## Note
- The instructions below help you install and run a local copy of the software on your computer for development purpose. It uses a remote database running on the [production server](http://farmview.herokuapp.com/), though.
- Updated on Sep 27 2017

## Requirements: for potential collaborators
- Farmview manages development environment using a virtual machine with common configurations to guarantee technical consistency across the collaborators and easier setup process.
  - We use [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
  - The shared provision script is supposed to install _all the required libraries and dependencies_.
- [Git](https://git-scm.com/downloads) command line tools

## Technical Specification
- Ubuntu 14.04.5 LTS
- Postgresql 9.3 or later (Only tested with version 9.3)
- Python 2.7.10 including pip (Not tested with Python 3)
- Django 1.9 or later
- (development only) UWSGI
- (development only) Nginx

## Instructions
- First, install the latest versions of [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
- Clone Farmview code repository to your local storage.
```
$ git clone https://github.com/stlim0730/farmview.git
```
- Create `local_settings.py` for Django server in `/farmview/farmview`.
  - This configuration file will affect your local instance of the software.
```
"""
local_settings.py
Local settings for development purpose
  local_settings.py must not exist on the production server
  or in the shared remote repository (GitHub).
"""

# Generate a Django secret key here:
#   https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '<your_django_secret_key>'

DEBUG = True

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'farmview',
    'USER': 'vagrant',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '5432'
  }
}
```
- Run vagrant to turn on the virtual machine (a.k.a. guest machine, in contrast to host machine).
  - For your initial setup, this command takes extra time (30-50 mins, depending on your internet speed) in downloading and installing Ubuntu and other dependencies.
  - Even after the initial setup, this command may take long (10-15 mins, depending on your internet speed) if it's fresh start (explained on teardown later).
```
# On your host machine
$ vagrant up
```
- Now you will be able to see the app running locally (http://localhost:8000).
- You may connect to the guest machine.
```
# On your host machine
$ vagrant ssh
```
- Quit the connection and get back to the host machine.
```
# On your guest machine
$ exit
```
- Even though the SSH connection has been quit, the guest machine is still running. There are three different types of teardown process. Refer to Vagrant documentation here: [Teardown](https://www.vagrantup.com/intro/getting-started/teardown.html).
```
# On your host machine
$ vagrant suspend

# or

$ vagrant halt

# or

$ vagrant destroy
```

## (Re-)Running the Server
- The Django server automatically starts when the guest machine boots up.
- You need to restart the server to apply changes made on backend code.
```
# On your guest machine
$ sudo service nginx restart
```

## Collaboration Workflow
TBD

## (working title) Dataflow and Database Prepopulation
TBD

## Deployment
TBD

## Admin Panel
- To access the admin panel of the software, you may click `Admin` on the sidebar menu or go to http://localhost:8888/admin
- Log in with your admin account.
- *Note that the changes you make here will directly affect both your local instance and the remote instance on the production server.*

### Basic Configurations
- Under `Map` section, click `Configs`.
- The software works based on the latest configuration in the list. If you want to update the configuration, press `add config` on the right.

### Datafields
- Under `Map` section, click `Datafields`.
- In this panel, you may config datafields to query about or display on the popup window when clicked.
- If the panel is empty, you can't make query to the database.
- Documentation for current settings is here (this documentation is now under extensive revision): https://docs.google.com/document/d/1bK6pKhQRQbSd9EzEprI12aMkCbYrvqmiwgYHuaNMz38/edit

### Translating
- in the command line run:
`django-admin.py makemessages -l es -e html,py`
- go into pages > locale > es > LC_MESSAGES and download the django.po file (Note: can directly edit .po file)
- upload file into https://translate.google.com/toolkit/list?hl=en#translations/active
- make changes
- redownload file
- replace old django.po file
- in the command line run:
`django-admin.py compilemessages`

## Blog
- The blog uses Zinnia. For the documentation, look here: 
- http://docs.django-blog-zinnia.com/en/develop/
- Use the text formatting guidelines according to Textile:
- https://txstyle.org/
