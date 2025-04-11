# seed.py
import csv
from app import app
from models import db, Episode, Guest, Appearance
import re

def seed_database():
    with app.app_context():
        # Clear all existing data
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        
        # Create tables
        db.create_all()
        
        # Dictionaries to track episodes and guests
        episodes_dict = {}
        guests_dict = {}
        
        with open('seed.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            
            episode_counter = 1
            guest_counter = 1
            
            for row in csv_reader:
                date = row['Show']
                
                # Creatting or getting episode
                if date not in episodes_dict:
                    # Extract the episode number from the date 
                    match = re.search(r'(\d+)/(\d+)/(\d+)', date)
                    if match:
                        month, day, year = match.groups()
                        episode_number = int(month) * 100 + int(day)  #creating a unique number
                    else:
                        episode_number = episode_counter
                    
                    episode = Episode(
                        id=episode_counter,
                        date=date,
                        number=episode_number
                    )
                    episodes_dict[date] = episode
                    db.session.add(episode)
                    episode_counter += 1
                
                guests = row['Raw_Guest_List'].split(", ")
                
                for guest_name in guests:
                    # Check if guest already exists
                    if guest_name not in guests_dict:
                        guest = Guest(
                            id=guest_counter,
                            name=guest_name,
                            occupation=row['GoogleKnowlege_Occupation']
                        )
                        guests_dict[guest_name] = guest
                        db.session.add(guest)
                        guest_counter += 1
                    
                    # Creatting  appearance and generate randomized rating between 1 and 5
                    import random
                    rating = random.randint(1, 5)
                    
                    appearance = Appearance(
                        rating=rating,
                        guest_id=guests_dict[guest_name].id,
                        episode_id=episodes_dict[date].id
                    )
                    db.session.add(appearance)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()