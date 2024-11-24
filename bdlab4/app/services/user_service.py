# app/services/user_service.py
from ..dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()

    @staticmethod
    def get_user(user_id):
        return UserDAO.get_user(user_id)

    @staticmethod
    def create_user(data):
        return UserDAO.create_user(data)

    @staticmethod
    def update_user(user_id, data):
        return UserDAO.update_user(user_id, data)

    @staticmethod
    def delete_user(user_id):
        return UserDAO.delete_user(user_id)
