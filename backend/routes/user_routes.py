from flask import request, jsonify, Blueprint
from controllers.user_controller import UserController

user_bp = Blueprint("user_bp", __name__)
user_controller = UserController()

@user_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_data = {
        "username": data.get("username"),
        "email": data.get("email"),
        "password": data.get("password"),
        "role": "regular"
    }
    new_user_id = user_controller.create_user(user_data)
    return jsonify({"msg": "User created successfully", "user_id": new_user_id}), 201

@user_bp.route("/api/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = user_controller.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route("/api/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if user_controller.update_user(user_id, data):
        return jsonify({"msg": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_controller.delete_user(user_id):
        return jsonify({"msg": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404
