# fastapicrud
Basic FastApi CRUD operation using sqlite

fastapicrud
A basic FastAPI application demonstrating CRUD operations using SQLite. The application allows you to add, retrieve, update, and delete user records in an SQLite database.

Features
Create: Add a new user to the database.

Read: Retrieve all users or a specific user by ID.

Update: Update an existing user's details.

Delete: Remove a user from the database.

Tech Stack
FastAPI: Web framework for building APIs.

SQLAlchemy: ORM to interact with SQLite database.

SQLite: Lightweight SQL database.

Project Structure

fastapicrud/
│
├── main.py               # Main FastAPI application
├── dbconfig.py           # Database configurations
└── requirements.txt      # Project dependencies

Installation
Clone the repository:

git clone https://github.com/TheAmityadav/fastapicrud.git
cd fastapicrud

Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate

Install the required dependencies:
pip install -r requirements.txt

Create the database:

The database schema will be automatically created when you run the application. However, if you want to manually check the database structure, you can inspect the dbconfig.py file.

Running the Application
To run the FastAPI application:

uvicorn main:app --reload
This will start the server on http://127.0.0.1:8000.