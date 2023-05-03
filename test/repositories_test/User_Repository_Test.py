from unittest import TestCase

from data.models.User import User
from data.repositories.User_Repository_Impl import User_Repository_Impl


class User_Repository_Test(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.userRepository = User_Repository_Impl()
        cls.user = User()

    def test_save_new_user_count_is_incremented(self):
        self.userRepository.save_user(self.user)
        self.assertEqual(1, self.userRepository.get_count_of_users())

    def test_save_two_same_user_count_does_not_increment(self):
        self.userRepository.save_user(self.user)
        self.userRepository.save_user(self.user)
        self.assertEqual(1, self.userRepository.get_count_of_users())

    def test_save_new_user_find_by_id(self):
        saved_user = self.userRepository.save_user(self.user)
        found_user = self.userRepository.find_user_by_id(saved_user.get_user_id())
        self.assertEqual(found_user, saved_user)
        self.assertEqual(1, self.userRepository.get_count_of_users())

    def test_save_new_user_find_user_by_email_and_password(self):
        self.user.set_email("alaabdulmalik03@gmail.com")
        self.user.set_password("ayanniyi@20")
        saved_user = self.userRepository.save_user(self.user)
        found_user = self.userRepository.find_user_by_email_and_password(saved_user.get_email(), saved_user.get_password())
        self.assertEqual(saved_user, found_user)
        self.assertEqual(1, self.userRepository.get_count_of_users())

    def test_save_new_user_find_user_by_phone_number_and_password(self):
        self.user.set_email("alaabdulmalik03@gmail.com")
        self.user.set_phone_number("07036174617")
        self.user.set_password("ayanniyi@20")
        saved_user = self.userRepository.save_user(self.user)
        found_user = self.userRepository.find_user_by_phone_number_and_password(saved_user.get_phone_number(), saved_user.get_password())
        self.assertEqual(saved_user, found_user)
        self.assertEqual(1, self.userRepository.get_count_of_users())

    def test_save_user_delete_user_by_id(self):
        self.user.set_email("alaabdulmalik03@gmail.com")
        self.user.set_phone_number("07036174617")
        self.user.set_password("ayanniyi@20")
        saved_user = self.userRepository.save_user(self.user)
        user_is_deleted = self.userRepository.delete_user_by_id(saved_user.get_user_id())
        self.assertEqual(0, self.userRepository.get_count_of_users())
        self.assertEqual(1, self.userRepository.get_count_of_deleted_users())
        self.assertTrue(user_is_deleted)
