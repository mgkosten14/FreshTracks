from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@main.route('/api/resorts', methods=['GET'])
def get_resorts():
    # Dummy resort data
    resorts = [
        {"name": "Snowy Peak", "state": "Colorado"},
        {"name": "Powder Heaven", "state": "Utah"}
    ]
    return jsonify(resorts)
