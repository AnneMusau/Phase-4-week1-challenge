from flask import Flask, jsonify, request
from models import db, Hero, Power, HeroPower
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask app
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 

# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the SQLAlchemy and Migrate instances
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict()), 200
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict()), 200
    return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get_or_404(id)
    data = request.get_json()
    if 'description' not in data or not data['description']:
        return jsonify({"errors":["description is required"]}),400
    if len (data['description']) < 20:
        return jsonify({"errors":["description must be at least 20 characters"]}), 400
    power.description = data['description']
    db.session.commit()
    power_dict = power.to_dict()
    return jsonify(power_dict),200

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    if "strength" in data and "power_id" in data and "hero_id" in data:
        hero_power = HeroPower(
            strength=data["strength"],
            power_id=data["power_id"],
            hero_id=data["hero_id"]
        )
        db.session.add(hero_power)  
        db.session.commit()  
        return jsonify(hero_power.to_dict()), 201 
    return jsonify({"errors": ["validation errors"]}), 400
        
if __name__ == '__main__':
    app.run(debug=True, port=5555)