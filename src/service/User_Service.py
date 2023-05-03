from abc import ABC, abstractmethod

from data.dto.request.Login_Request import Login_Request
from data.dto.request.UserRequest import User_Request
from data.dto.response.User_Response import User_Response


class User_Service(ABC):
     
    @abstractmethod
    def register_new_user(self, request: User_Request) -> User_Response:
        pass

    @abstractmethod
    def find_registered_user_by_id(self, user_id: str) -> User_Response:
        pass

    @abstractmethod
    def find_registered_user_by_email_and_password(self, request: User_Request) -> User_Response:
        pass

    @abstractmethod
    def find_registered_user_by_phone_number_and_password(self, request: User_Request) -> User_Response:
        pass

    @abstractmethod
    def delete_user_by_id(self, userId: str) -> str | None:
        pass

    @abstractmethod
    def get_count_of_users(self) -> int:
        pass

    @abstractmethod
    def get_count_deleted_of_users(self) -> int:
        pass

    @abstractmethod
    def login_existing_user(self, login_request: Login_Request):
        pass

    @abstractmethod
    def update_existing_user(self, user_request: User_Request) -> User_Response:
        pass
