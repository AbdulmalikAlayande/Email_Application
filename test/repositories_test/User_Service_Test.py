from unittest import TestCase

from data.dto.request.Login_Request import Login_Request
from data.dto.request.UserRequest import User_Request
from data.dto.response.User_Response import User_Response
from service.User_Service_Impl import User_Service_Impl


class User_Service_Test(TestCase):

    def setUp(self) -> None:
        self.user_service = User_Service_Impl()
        self.user_request = User_Request()
        self.user_response = User_Response()
        self.user_request.set_user_name("Abdulmalik")
        self.user_request.set_email("alaabdulmalik03@gmail.com")
        self.user_request.set_password("ayanniyi@20")
        self.user_request.set_phone_number("07036174617")
        self.user_response = self.user_service.register_new_user(self.user_request)

    def test_that_users_can_register_a_new_account(self):
        self.assertEqual(1, self.user_service.get_count_of_users())

    def test_register_new_user_find_registered_user_by_id(self):
        found_user = self.user_service.find_registered_user_by_id(self.user_response.get_user_id())
        self.assertEqual(found_user.get_user_id(), self.user_response.get_user_id())

    def test_register_new_user_find_registered_user_by_email_and_password(self):
        found_user = self.user_service.find_registered_user_by_email_and_password(self.user_request)
        self.assertIsNotNone(found_user)

    def test_register_new_user_find_registered_user_by_phone_number_and_password(self):
        found_user = self.user_service.find_registered_user_by_phone_number_and_password(self.user_request)
        self.assertIsNotNone(found_user)

    def test_register_new_user_delete_registered_user_by_id(self):
        deleted = self.user_service.delete_user_by_id(self.user_response.get_user_id())
        self.assertEqual("account successfully deleted", deleted)
        self.assertEqual(0, self.user_service.get_count_of_users())
        self.assertEqual(1, self.user_service.get_count_deleted_of_users())

    def test_that_user_can_login(self):
        service = User_Service_Impl()
        request = User_Request()
        request.set_user_name("gorimapa")
        request.set_password("ayanniyi@20")
        request.set_email("alaabdulmalik03@gamil.com")
        request.set_phone_number("09066641977")
        service.register_new_user(request)
        login_request = Login_Request()
        login_request.set_email("alaabdulmalik03@gamil.com")
        login_request.set_password("ayanniyi@20")
        login_request.set_phone_number("09066641977")
        logged_in_user = self.user_service.login_existing_user(login_request)
        self.assertEqual(logged_in_user, request)

    def test_save_user_multiple_times_count_does_not_increment(self):
        service = User_Service_Impl()
        request = User_Request()
        request.set_user_name("gorimapa")
        request.set_password("gorilla")
        request.set_email("gorigori@gmail.com")
        request.set_phone_number("09066641977")
        saved_user = service.register_new_user(request)
        self.assertIsNotNone(saved_user.get_user_id())
        self.assertEqual(1, service.get_count_of_users())

        found_user = service.find_registered_user_by_phone_number_and_password(request)
        self.assertIsNotNone(found_user.get_user_id())

        request.set_email("fe@gmail.com")
        service.update_existing_user(request)
        self.assertEqual(1, service.get_count_of_users())
