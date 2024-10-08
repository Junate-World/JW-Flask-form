User Information Collector
=====================================

A Flask application to collect and manage user information.

Overview
This application uses Flask and Flask-SQLAlchemy to create a simple user information collector. It allows users to submit their information through a form, which is then stored in a SQLite database. The application also provides a route to view all collected user information and edit individual user records. It also include static asset. 

Features
User information collection through a form
Storage of user information in a SQLite database
Route to view all collected user information
Route to edit individual user records

Requirements
Flask
Flask-SQLAlchemy
SQLite

Installation
Clone the repository: git clone https://github.com/Junate-World/JW-Flask-form.git
Install the required packages: pip install -r requirements.txt
Create a new SQLite database: sqlite3 users.db
Run the application: python app.py

Routes
/: Collect user information through a form
/users: View all collected user information
/edit/<int:user_id>: Edit individual user records

Models
User: Represents a user's information, with attributes for name, email, phone, address, city, state, zip code, country, occupation, company, and comment.

Templates
form.html: The form to collect user information
users.html: The page to view all collected user information

Configuration
SQLALCHEMY_DATABASE_URI: The URI of the SQLite database
SECRET_KEY: A secret key for the application

Running the Application
Run the application: python app.py
Open a web browser and navigate to http://localhost:5000
Fill out the form to collect user information
View all collected user information at http://localhost:5000/users
Edit individual user records at http://localhost:5000/edit/<int:user_id>#   J W - F l a s k - f o r m  
 