# Farmview

## Note
- The instructions below help you install and run a local copy of the software on your computer for development purpose. It still uses remote data on [Carto](https://carto.com/).
- Updated on Oct 21 2017

## Requirements: for potential collaborators
- Farmview manages development environment using a virtual machine with static configurations to guarantee technical consistency across the collaborators and easier setup process.
  - We use [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
  - The shared provision script is supposed to install all the required libraries and dependencies.
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

- Now you will be able to see the app running locally (http://localhost:8888).
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

- I usually suspend the guest machine when I wrap up a coding or a testing session. I destroy the guest machine when I want to explicitly run provision (including Python package installation) script of vagrant.

## (Re-)Running the Server
The Django server automatically starts when the guest machine boots up.

Nginx server uses UWSGI module as an app container for Django. When you made changes in Django backend, use the command below to restart Django app.

```
# On your guest machine
$ touch reload.ini
```

In general, you don't need to restart Nginx server. When you have to, use the command below.

```
# On your guest machine
$ sudo service nginx restart
```

## Collaboration Workflow
You should follow standard Git workflow to guarantee traceable states of your contribution and the integrity of the shared codebase. Please refer to the suggested workflow as follows.

### Branching
Once you cloned the remote repository to your local storage, before you make changes in code:

```
$ git checkout -b my-branch
Switched to a new branch 'my-branch'
```

This command is a shortcut equivalent to a sequence of two commands below, which creates a new branch and switch to the new branch.

```
$ git branch my-branch
$ git checkout my-branch
```

The shortcut prevents a potential mistake that you create a new branch and work on the old one (usually `master`).
In that sense, it's important to be always aware of the branch you're on.

```
$ git branch
  master
* my-branch
```

It's strongly recommended that you create a branch before you make changes in your code. However, even if you have already made changes (on `master` branch), you may (and should) create a new branch using the same command BEFORE you make *commits*. The command to create a new branch copies all the changes on the current branch to the new branch. Copying all the changes you made on the current branch is implicit process, which we don't love in using Git. So, always try to create a new branch before you work on the code.

Naming is an essential skill to a software engineer! Always try to use concise and descriptive branch name (I admit my-branch is a terrible example!).

### Coding
Have fun!

### Commit
Commit is making a checkpoint. All commit should represent a valid state of the codebase.

Lookup what files have been changed or created.

```
$ git status
```

Stage the files you want to include in this commit.

```
$ git add <filename>
```
TBD: add

### Push
TBD

### Pull Request
TBD

### Merge
TBD

## Deployment
Farmview is currently using [Heroku](https://www.heroku.com) as the hosting solution. Similarly to our development environment, the production server needs all the software dependencies installed. Heroku, like other PAAS (platform as a service) providers, has well-pipelined provision & deployment tools. All we should do is maintain the scripts specifying the configurations that Farmview relies on.

Heroku provides a useful set of command line tools for deployment, but I would discourage you from using it. Deployment is a critical step in a sense that the `master` branch in the shared repository gets accessible to the public. This critical process has to be non-automatic and carefully controlled, rather than getting pushed directly from `master` branch on a local machine to the server. Instead, we use web-based admin [dashboard](https://dashboard.heroku.com/apps/farmview/deploy/github) on Heroku as an explicit step (or the final gate keeper) for deployment. Heroku's dashboard talks directly to GitHub repository and fetches a branch specified. When a deployment request is made, installation, compilation, and configuration of the dependencies automatically precede the deployment. If you need the deployment permission on Heroku, contact the repository owner.

## (working title) Dataflow and Database Prepopulation
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
