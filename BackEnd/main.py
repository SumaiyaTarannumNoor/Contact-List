from flask import request, jsonify
from config import app, db
from models import Contact

@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route('/create_contact', methods=['POST'])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or last_name or not email:
        return jsonify({"message": "You must fill up all the fields."}, 400)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)