# World Website
## About 
This project aims to streamline CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database through web interfaces built using two popular Python frameworks: Django and Flask. With a user-friendly interface, it enables efficient management of data across three interconnected tables: continents, countries, and cities.
## Installation and Setup

***All of the following commands need to be done inside the 'world_website' folder or targeted to 'manage.py' file inside the world_website folder***

1. **Install Dependencies:**

   ```bash
    pip install -r requirements.txt
    cd world_website
    python manage.py loaddata data.json
    ```

    ***This will install all the dependencies and load the data from the 'data.json' file into the database.***

2. **You can create a super user:**

    ***To see the admin page go to <http://127.0.0.1:8000/admin/>***

    ```bash
    python manage.py createsuperuser
    ```

3. **Run Server:**

    ```bash
    python manage.py runserver
    ```
