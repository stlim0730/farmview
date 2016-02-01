#Farmview
##Note
- The instructions below help you install and run a copy of the software on your computer for development purpose. It uses a remote database running on the production server, though (http://farmview.herokuapp.com/).
- Updated on Feb 1 2016

##Requirements
- Git command line tools (https://git-scm.com/downloads)
- Python 2.7.10 (https://www.python.org/)
- Django 1.8 (https://www.djangoproject.com/)

##Instructions
- If you don't have the right versions of the prerequisites, follow the installation guide here (you may skip *Set up a database* section as this software uses a remote database): https://docs.djangoproject.com/en/1.8/intro/install/
- After the installation, clone this repository.
```
git clone https://github.com/stlim0730/farmview.git
```

##Running the Server
- Run a server instance.
```
python manage.py runserver
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

###Query Fields
- Under `Map` section, click `Query fields`.
- In this panel, you may config data fields to query about.
- If the panel is empty, you can't make query to the database.
- Documentation for current settings is here: https://docs.google.com/document/d/1bK6pKhQRQbSd9EzEprI12aMkCbYrvqmiwgYHuaNMz38/edit
