# Flask application setup

from flask import Flask,jsonify,request,make_response
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/episodes',methods=['GET'])
def get_episodes():
    episodes=Episode.query.all()
    return jsonify([{
        'id':episode.id,
        'date':episode.date,
        'number':episode.number
    } for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    
    return jsonify(episode.to_dict(rules=('-appearances.episode',)))

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests])


@app.route('/appearances',methods=['POST'])
def create_appearance():
    data=request.get_json()

    try:
        episode=Episode.query.get(data['episode_id'])
        guest=Guest.query.get(data['guest_id'])

        if not episode or not guest:
            return make_response(jsonify({'error':'Episode or guest not found'}),404)
            
        new_appearance=Appearance(
            rating=data.get('rating'),
            episode_id=data.get('episode_id'),
            guest_id=data.get('guest_id')
        )

        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict())
    
    except Exception as e:
        return jsonify({"errors":[str(e)]}),400
    
if __name__ == '__main__':
    app.run(debug=True, port=5555)# port 5555 to match the one running on postman url