#Farmview
##Note
- The instructions below help you install and run a copy of the software on your computer. It uses a remote database running on the production server, though (http://farmview.herokuapp.com/).

##Requirements
- Git command line tools (https://git-scm.com/downloads)
- Python 2.7.10 (https://www.python.org/)
- Django 1.8 (https://www.djangoproject.com/)

##Instructions
- If you don't have the right versions of Python or Django, follow the installation guide here (you may skip `Set up a database` section as this software uses a remote database): https://docs.djangoproject.com/en/1.8/intro/install/
- After the installation, clone this repository.
```
git clone https://github.com/stlim0730/farmview.git
```

##Converting Survey Questionnaire
- This software includes a command line tool that converts an XLS Form for the survey into a JSON representation of the questionnaire. The JSON file will be used to populate the database.
- Go to the project directory.
```
cd farmview
```
- The conversion tool is located in mapper directory.
```
cd mapper
```
- Run the conversion tool using the command as follows. Replace the input / output file names with your actual file names.
```
python converter.py question_inputfile.csv choice_inputfile.csv question_outputfile.json choice_outputfile.json
```

##Running the Server
- Run a server instance.
```
python manage.py runserver
```
- If you're using one of UNIX systems including Mac OS X, you may use this shortcut.
```
./run
```
- Your terminal will show the localhost IP (e.g., http://127.0.0.1:8000/). Put the IP in your web browser's address bar.

##Admin Panel
- To access the admin panel of the software, you may click `Admin` on the sidebar menu or go to http://127.0.0.1:8000/admin
- Log in with your admin account.
- *Note that the changes you make here will directly affect both your local instance and the remote instance on the production server.*

###Basic Configurations
- Under `Mapper` section, click `Configs`.
- The software works based on the latest configuration in the list. If you want to update the configuration, press `add config` on the right.

###Survey Questions
- In this panel, you may choose data fields about which a user can query using the software.
- If the panel is empty, import the converted question JSON file.
- Select checkboxes of the survey questions you want to make queryable.
- In the `action` menu (at the top of the list), select `Mark selected fields as queryable`.
- Press `Go` button.

###Survey Choices
- Currently, there's nothing to do in this panel. Use this panel for reference.
- If the panel is empty, import the converted choice JSON file.
