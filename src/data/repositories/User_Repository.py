from abc import ABC, abstractmethod
from typing import List

from data.models.User import User


class User_Repository(ABC):

    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user_by_id(self, userId: str) -> User:
        pass

    @abstractmethod
    def find_user_by_email_and_password(self, email: str, password: str) -> User:
        pass

    @abstractmethod
    def find_user_by_phone_number_and_password(self, phone_number: str, password: str):
        pass

    @abstractmethod
    def find_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def delete_user_by_id(self, userId: str) -> bool:
        pass

    @abstractmethod
    def get_count_of_users(self):
        pass

    @abstractmethod
    def get_count_of_deleted_users(self):
        pass
