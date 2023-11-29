# INF553 Django Web App
By Anthony Saab and Peter Farah

# Environment Checklist
To run this project on your own environment, you will need:

## Libraries and Programs
- Python 3.11 installed
- pip 23.2.1 installed
- Python packages listed in requirements.txt installed using pip

## Environment Variables 
The variables needed are used for setting up a connection between the Web APP and the relevant, populated PostGreSQL DB
- GRES_DBNAME which is the DB's name
- GRES_USER which is the relevant username to login into the DB
- GRES_PASS which is the relevant password to login into the DB
- GRES_HOST which is the IP address of the host running the DB
- GRES_PORT which is the Port Number of the DB

## Running the project
- Open a terminal
- Navigate to the directory where manage.py and requirements.txt of this project are located
- Run "python manage.py runserver"

For any additional guidance concerning Django, visit https://docs.djangoproject.com/en/4.2/ for the official documentation
