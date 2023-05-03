from data.dto.request.UserRequest import User_Request
from data.dto.response.User_Response import User_Response
from data.models.User import User


class Mapper:

    def map(self, request_or_user_to_map: User or User_Request) -> User | User_Response:
        if isinstance(request_or_user_to_map, User):
            return self.map_user_to_response(request_or_user_to_map)
        elif isinstance(request_or_user_to_map, User_Request):
            return self.map_request_to_user(request_or_user_to_map)

    @staticmethod
    def map_user_to_response(user) -> User_Response:
        response = User_Response()
        response.set_user_name(user.get_user_name())
        response.set_email(user.get_email())
        response.set_password(user.get_password())
        response.set_user_id(user.get_user_id())
        response.set_phone_number(user.get_phone_number())
        return response

    @staticmethod
    def map_request_to_user(request) -> User:
        user = User()
        user.set_user_name(request.get_user_name())
        user.set_email(request.get_email())
        user.set_phone_number(request.get_phone_number())
        user.set_password(request.get_password())
        return user
