#Late Show API
This projects Implements a FLASK API for managing data about late sow episodes, guests and their appearances.
The lateshow API provides endpoints to:
-View all episodes from the Late Show
-View specific episodes with their guest appearances
-View all guests who have appeared on the show
-Create new appearance records for guests on episodes

#Installation
1. Clone the repository:git clone git@github.com:Nzyoki/lateshow-scola-nzyoki.git 
2.cd to lateshow-scola-nzyoki
3.Create a Virtual env on the terminal and activaate it:
-python3 -m venv venv
-source venv/bin/activate
4.Install the dependancies
-pip install flask flask-sqlalchemy flask-migrate sqlalchemy-serializer
5. Seed the database with episode and guest data
-python seed.py
6.Start the server on port 5555(which I used to test on Postman)
7. The Server will start running on http://localhost:5555/

#Database Structure
The database has 3 models:
##Episode
-id: Primary key
-date: Date of the episode
-number: Episode number
##Guest
-id: Primary key
-name: Guest's name
-occupation: Guest's occupation
##Appearance
-An Episode has many Guests through Appearance
-A Guest has many Episodes through Appearance
-An Appearance belongs to both a Guest and an Episode

#API endpoints
##Get episodes
-Returns a list of all episodes
##GET/episodes/
-Returns details for a specific episode with all its associated guest appearances.
N/B:If the episode doesn't exist, returns:
##GET /guests
-Returns a list of all guests.
##POST /appearances
-Creates a new appearance record.
N/B:Error response (if validation fails):"errors": ["Rating must be between 1 and 5"]

#To test on Postman, make sure that python app.py is running so as to run the endpoints on postman.
image.png
image.png
image.png