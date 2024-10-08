SUPERHERO API

#Project Overview
The Superhero API is a RESTful API built using Flask and SQLAlchemy that allows users to manage a collection of superheroes and their powers. This project implements CRUD operations to manage superheroes, their attributes, and their powers. The API is designed to be easily extensible and testable using Postman.

#Features
Add, retrieve, update, and delete superheroes.
Assign powers to superheroes.
Retrieve and update superhero powers.
Relationship management between superheroes and their powers.

#Technologies Used
Python 3.12+: Backend language.
Flask: Web framework for building the API.
SQLAlchemy: ORM (Object Relational Mapping) for interacting with the database.
SQLite: Lightweight, file-based database.
Postman: For testing API routes.

#Requirements
Python 3.12+
Flask
Flask-SQLAlchemy
Postman (for testing)
SQLite3 (default database for this project)

#Setup and Installation
1. Clone the Repository
~~~bash
Copy code
git clone https://github.com/annemusau/superhero-api.git
cd superhero-api
2. Create and Activate Virtual Environment
~~~bash
Copy code
python -m venv venv
source venv/bin/activate 
3. Install Dependencies
~~~bash
Copy code
pip install pipenv
pipenv install
4. Set Up the Database
Initialize the database by creating all the tables and applying migrations:

~~~bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
5. Seed the Database
To populate the database with sample data:

~~~bash
Copy code
python server/seed.py
6. Running the Application
Start the Flask server by running:

~~~bash
Copy code
cd server
flask run
The server will start at http://127.0.0.1:5000/.

#API Endpoints
Here are the available API endpoints. You can use Postman or any HTTP client to test these routes.

#Superheroes
HTTP Method	Endpoint	Description
GET	/heroes	Get a list of all superheroes
GET	/heroes/<id>	Get details of a specific superhero
POST	/heroes	Create a new superhero
PATCH	/heroes/<id>	Update a superhero's details
DELETE	/heroes/<id>	Delete a superhero

#Powers
HTTP Method	Endpoint	Description
GET	/powers	Get a list of all powers
GET	/powers/<id>	Get details of a specific power
PATCH	/powers/<id>	Update power details

#Superhero Powers
HTTP Method	Endpoint	Description
POST	/heroes/<id>/powers	Add powers to a specific superhero

#Testing the API
You can test the API endpoints using Postman by importing the provided Postman collection file:

#Open Postman and click Import.
Select the challenge-2-superheroes.postman_collection.json file from the project directory.
Once imported, you can run the collection and test the API endpoints.
Example Request - Create a Superhero
POST /heroes

Request Body:

~~~json
Copy code
{
  "name": "Bruce Wayne",
  "super_name": "Batman"
}
Response:

~~~json
Copy code
{
  "id": 1,
  "name": "Bruce Wayne",
  "super_name": "Batman",
  "powers": []
}
#Database Models
#Hero
Attribute	Type	Description
id	Integer	Unique identifier for hero
name	String	Hero's real name
super_name	String	Hero's superhero alias
#Power
Attribute	Type	Description
id	Integer	Unique identifier for power
name	String	Name of the power
description	String	Description of the power

#Project Structure
~~~bash
Copy code
superhero-api/
├── Pipfile
├── Pipfile.lock
└── server
    ├── Readme.md
    ├── __pycache__
    │   ├── app.cpython-312.pyc
    │   └── models.cpython-312.pyc
    ├── app.py
    ├── instance
    │   └── database.db
    ├── migrations
    │   ├── README
    │   ├── __pycache__
    │   │   └── env.cpython-312.pyc
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       ├── __pycache__
    │       │   └── ba51dcc1d84e_initial_migration.cpython-312.pyc
    │       └── ba51dcc1d84e_initial_migration.py
    ├── models.py
    └── seed.py
#Future Enhancements
Add user authentication to restrict access to specific endpoints.

#Licence
This project is licensed under the MIT License.

Author
Anne Moige Musau - GitHub
