There is currently 3 user: erdem.ontas, test2, test3
They have some tasks on themn.

To create a new user go to localhost:8000/register
To login go to  localhost:8000/accounts/login
To logout go to  localhost:8000/accounts/logout

Swagger has implemented to the project so you can use there as well.

Installation



    Clone Project:

    git clone https://github.com/erdemontas/todoapp-dev.git

    Install virtual environment

    python3 -m venv env

    Activate virtual env

        on Mac OS or Linux --> source env/bin/activate

        on Windows --> .\env\Scripts\activate.bat

    Install all requirements:

    pip install -r requirements.txt

    Start Django Application:

    cd 'Project folder'
    python manage.py makemigrations
    python manage.py migrate

    Create a super user:

    python manage.py createsuperuser

    Run Server:

    python manage.py runserver localhost:8000
