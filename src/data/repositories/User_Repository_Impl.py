from typing import List

from data.models.User import User
from data.repositories.User_Repository import User_Repository
from utils.Id_Generator import Id_Generator


class User_Repository_Impl(User_Repository):

    def __init__(self):
        self._list_of_users: List[User] = []
        self._list_of_deletes_users: List[User] = []

    def save_user(self, user: User) -> User:
        if user.get_user_id() == "" and user not in self._list_of_users:
            self._save_new_user(user)
        return self._existing_user(user)

    def _save_new_user(self, user: User) -> User:
        user.set_user_id(self._generatedId())
        self._list_of_users.append(user)
        return user

    def _existing_user(self, user) -> User:
        found_user = self.find_user_by_id(user.get_user_id())
        return found_user

    def find_user_by_id(self, userId: str) -> User | None:
        for user in self._list_of_users:
            if user.get_user_id() == userId:
                return user
        return None

    def find_all_users(self) -> List[User]:
        return self._list_of_users

    def find_user_by_email_and_password(self, email: str, password: str) -> User | None:
        for user in self._list_of_users:
            if user.get_email() == email and user.get_password() == password:
                return user
        return None

    def find_user_by_phone_number_and_password(self, phone_number: str, password: str) -> User | None:
        for user in self._list_of_users:
            if user.get_phone_number() == phone_number and user.get_password() == password:
                return user
        return None

    def delete_user_by_id(self, userId: str) -> bool:
        for user in self._list_of_users:
            if user.get_user_id() == userId:
                self._list_of_deletes_users.append(user)
                self._list_of_users.remove(user)
        is_deleted: bool = self.find_user_by_id(userId) is None
        return is_deleted

    def get_count_of_users(self) -> int:
        return len(self._list_of_users)

    def _generatedId(self) -> str:
        return Id_Generator.generate_id(self._list_of_users)

    def get_count_of_deleted_users(self) -> int:
        return len(self._list_of_deletes_users)
