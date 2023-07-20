from models.user import UserSchema
from app import mongo

class UserController:
    def create_user(self, user_data):
        result = mongo.db.users.insert_one(user_data)
        return str(result.inserted_id)

    def get_user_by_id(self, user_id):
        user_data = mongo.db.users.find_one({"_id": user_id})
        if user_data:
            user_data["_id"] = str(user_data["_id"])
            return user_data
        else:
            return None

    def update_user(self, user_id, update_data):
        result = mongo.db.users.update_one({"_id": user_id}, {"$set": update_data})
        return result.modified_count > 0

    def delete_user(self, user_id):
        result = mongo.db.users.delete_one({"_id": user_id})
        return result.deleted_count > 0
