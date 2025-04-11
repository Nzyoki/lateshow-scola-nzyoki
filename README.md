Late Show API
-This project implements a Flask API for managing data about Late Show episodes, guests, and their appearances.

Features
The Late Show API provides endpoints to:

-View all episodes of the Late Show

-View a specific episode with guest appearances

-View all guests who have appeared on the show

-Create new appearance records linking guests and episodes

Installation & Setup
Clone the repository
git clone git@github.com:Nzyoki/lateshow-scola-nzyoki.git

Navigate into the project directory
cd lateshow-scola-nzyoki

Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

Install the dependencies
pip install flask flask-sqlalchemy flask-migrate sqlalchemy-serializer

Seed the database
python seed.py

Run the server
python app.py
The server will start at: http://localhost:5555

Database Structure
1.Episode
id: Primary key
date: Date of the episode
number: Episode number

2.Guest
id: Primary key
name: Guest's name
occupation: Guest's occupation

3.Appearance
An Episode has many Guests through Appearance
A Guest has many Episodes through Appearance
An Appearance belongs to both a Guest and an Episode

API Endpoints
1.Get All Episodes
GET /episodes
Returns a list of all episodes

2.Get Specific Episode
GET /episodes/int:id
Returns details for a specific episode, including all associated guest appearances

3.If the episode does not exist, returns:
{ "error": "Episode not found" }

4.Get All Guests
GET /guests
Returns a list of all guests

5.Create Appearance
POST /appearances
Creates a new appearance record

Expected request body:

{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 2
}
6.Error response if validation fails:

{
  "errors": ["Rating must be between 1 and 5"]
}

Testing with Postman
To test the endpoints using Postman:

Ensure the server is running:
python app.py
Use the base URL: http://localhost:5555

Make requests to the endpoints described above.