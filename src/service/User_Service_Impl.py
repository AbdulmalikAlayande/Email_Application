from data.dto.request.Login_Request import Login_Request
from data.dto.request.UserRequest import User_Request
from data.dto.response.User_Response import User_Response
from data.models.User import User
from data.repositories.User_Repository_Impl import User_Repository_Impl
from service.User_Service import User_Service
from utils.Mapper import Mapper


class User_Service_Impl(User_Service):

    def __init__(self):
        self.user_repository = User_Repository_Impl()
        self.mapper = Mapper()

    def register_new_user(self, request: User_Request) -> User | User_Response:
        # todo: i have to make sure that multiple users do not have same email
        user = self.mapper.map(request)
        self.user_repository.save_user(user)
        response = self.mapper.map(user)
        return response

    def login_existing_user(self, user_request: Login_Request):
        user_found_by_phone_number = self.user_repository.find_user_by_phone_number_and_password(user_request.get_phone_number(), user_request.get_password())
        print("user found is: " + user_found_by_phone_number.__str__())
        print("all users are: " + self.user_repository.find_all_users().__str__())
        user_found_by_email = self.user_repository.find_user_by_email_and_password(user_request.get_email(), user_request.get_password())

        if user_found_by_email in self.user_repository.find_all_users() or user_found_by_phone_number in self.user_repository.find_all_users():
            return user_found_by_email or user_found_by_phone_number
        return "invalid log in details"

    def update_existing_user(self, user_request: User_Request) -> User_Response:
        found_user: User = self.user_repository.find_user_by_phone_number_and_password(user_request.get_phone_number(),
                                                                                       user_request.get_password())
        print("The found user in the update method is: " + found_user.__str__())
        self._update_user_details(found_user)
        saved_user = self.user_repository.save_user(found_user)
        print("The saved user after re-saving is: " + saved_user.__str__())
        response = self.mapper.map(saved_user)
        return response

    def _update_user_details(self, found_user):
        # todo i need to collect prompt sha to be able to implement this method, so am coming back to you.
        pass

    def find_registered_user_by_id(self, user_id: str) -> User_Response:
        found_user = self.user_repository.find_user_by_id(user_id)
        return self.mapper.map(found_user)

    def find_registered_user_by_email_and_password(self, request: User_Request) -> User_Response:
        found_user = self.user_repository.find_user_by_email_and_password(request.get_email(), request.get_password())
        return self.mapper.map(found_user)

    def find_registered_user_by_phone_number_and_password(self, request: User_Request) -> User_Response:
        found_user = self.user_repository.find_user_by_phone_number_and_password(request.get_phone_number(),
                                                                                 request.get_password())
        return self.mapper.map(found_user)

    def delete_user_by_id(self, userId: str) -> str | None:
        is_deleted: bool = self.user_repository.delete_user_by_id(userId)
        if is_deleted: return "account successfully deleted"
        return None

    def get_count_of_users(self) -> int:
        return self.user_repository.get_count_of_users()

    def get_count_deleted_of_users(self) -> int:
        return self.user_repository.get_count_of_deleted_users()
