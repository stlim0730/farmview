#Farmview
##Note
- The instructions below help you install and run a copy of the software on your computer for development purpose. It uses a remote database running on the production server, though (http://farmview.herokuapp.com/).
- Updated on Mar 27 2016

##Requirements
- Git command line tools (https://git-scm.com/downloads)
- Python 2.7.10 or later (https://www.python.org/) including pip
- Django 1.9 or later (https://www.djangoproject.com/)
- 
##Instructions
- If you don't have the prerequisites, follow the installations below.
- Install Django using Python package management system
- (Running from a virtualenv may be helpful with djangotool box and simplejson installed with pip)
```
pip install Django
```
- You need to install `psycopg2` Python package, which is the PostgreSQL database driver for Python. Since Farmview team experienced that Django often fails to find PostgreSQL configurations installed via MacPorts, We strongly recommend installing the package via Homebrew (http://brew.sh/).
```
brew install psycopg2
```
- After the installation, clone this repository.
```
git clone https://github.com/stlim0730/farmview.git
```

##Running the Server
- Run a server instance.
```
python manage.py runserver (this may be preferable to ./run if you are having installation issues)
```
- If you're using a UNIX system including Mac OS X, you may use this shortcut.
```
./run
```
- Your terminal will show the localhost IP (e.g., http://127.0.0.1:8000/). Put the IP in your web browser's address bar.

##Admin Panel
- To access the admin panel of the software, you may click `Admin` on the sidebar menu or go to http://127.0.0.1:8000/admin
- Log in with your admin account.
- *Note that the changes you make here will directly affect both your local instance and the remote instance on the production server.*

###Basic Configurations
- Under `Map` section, click `Configs`.
- The software works based on the latest configuration in the list. If you want to update the configuration, press `add config` on the right.

###Datafields
- Under `Map` section, click `Datafields`.
- In this panel, you may config datafields to query about or display on the popup window when clicked.
- If the panel is empty, you can't make query to the database.
- Documentation for current settings is here (this documentation is now under extensive revision): https://docs.google.com/document/d/1bK6pKhQRQbSd9EzEprI12aMkCbYrvqmiwgYHuaNMz38/edit

###Translating
<<<<<<< HEAD
- Make edits in the .html or .py file
- if adding text but 
=======
- Make edits in the .html or .py file (if inserting new text, wrap text with `{% trans "new text here" %}`)
>>>>>>> 77cd4ca97211f68858814362c1eca9d515ac6c30
- in the command line run:
`django-admin.py makemessages -l es -e html,py`
- go into pages > locale > es > LC_MESSAGES and download the django.po file (Note: can directly edit .po file)
- upload file into https://translate.google.com/toolkit/list?hl=en#translations/active
- make changes
- redownload file
- replace old django.po file
- in the command line run:
<<<<<<< HEAD
`django-admin.py compilemessages`
=======
`django-admin.py compilemessages`
>>>>>>> 77cd4ca97211f68858814362c1eca9d515ac6c30
