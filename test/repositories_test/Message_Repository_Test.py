from typing import List
from unittest import TestCase

from data.models.Message import Message
from data.repositories.Message_Repository_Impl import Message_Repository_Impl


class Message_Repository_Test(TestCase):

    def setUp(self) -> None:
        self.message_repository = Message_Repository_Impl()
        self.message = Message()
        self.message.set_recipient_email("alabdulmalik03@gmail.com")
        self.message.set_sender_email("a.abdulmalik@native.semicolon.africa")
        self.message.set_user_id("1234")
        self.message.set_folder_id("3456")
        self.saved_message = self.message_repository.save_message(self.message)

    def test_save_message_count_is_incremented(self):
        self.assertEqual(1, self.message_repository.get_count_of_all_messages())
        print("The user id is: " + self.saved_message.get_user_id())
        self.assertEqual(1, self.message_repository.get_count_of_all_messages_per_user_by_user_id(
            self.saved_message.get_user_id()))

    def test_save_message_multiple_times_count_is_not_incremented(self):
        self.message_repository.save_message(self.saved_message)
        self.assertEqual(1, self.message_repository.get_count_of_all_messages())

    def test_save_message_get_message_by_recipient_email_and_message_id(self):
        found_message = self.message_repository.find_message_by_recipient_email_and_message_id(
            self.saved_message.get_recipient_email(), self.saved_message.get_message_id())
        self.assertIsNotNone(found_message)

    def test_save_message_get_message_by_sender_email_and_message_id(self):
        found_message = self.message_repository.find_message_by_sender_email_and_message_id(
            self.saved_message.get_sender_email(), self.saved_message.get_message_id())
        self.assertIsNotNone(found_message)

    def test_save_message_get_message_by_message_id(self):
        found_message = self.message_repository.find_message_by_message_id(self.saved_message.get_message_id())
        self.assertIsNotNone(found_message)

    def test_get_all_messages(self):
        message1 = Message()
        message1.set_sender_email("abdl@gmail.com")
        message1.set_recipient_email("weret@gmail.com")
        message1.set_user_id("5678")
        message1.set_folder_id("3456")
        self.message_repository.save_message(message1)
        list_of_messages: List[Message] = [self.message, message1]
        self.assertListEqual(list_of_messages, self.message_repository.get_all_messages())

    def test_get_all_messages_for_a_particular_user(self):
        message1 = Message()
        message1.set_sender_email("abdl@gmail.com")
        message1.set_recipient_email("weret@gmail.com")
        message1.set_user_id("1234")
        self.message_repository.save_message(message1)
        list_of_messages: List[Message] = [self.message, message1]
        self.assertListEqual(list_of_messages, self.message_repository.get_all_messages_per_user("1234"))

    def test_save_message_delete_message_by_message_id(self):
        is_deleted_message: bool = self.message_repository.delete_message_by_message_id(
            self.saved_message.get_message_id())
        self.assertTrue(is_deleted_message)
        self.assertEqual(0, self.message_repository.get_count_of_all_messages())
        self.assertEqual(0, self.message_repository.get_count_of_all_messages_per_user_by_user_id(
            self.saved_message.get_user_id()))

    def test_save_message_delete_message_by_message_id_recipient_email(self):
        is_deleted_message: bool = self.message_repository.delete_message_by_message_id_and_recipient_email(
            self.saved_message.get_message_id(), self.message.get_recipient_email())
        self.assertTrue(is_deleted_message)
        self.assertEqual(0, self.message_repository.get_count_of_all_messages())
        self.assertEqual(0, self.message_repository.get_count_of_all_messages_per_user_by_user_id(
            self.saved_message.get_user_id()))

    def test_save_message_delete_message_by_message_id_sender_email(self):
        is_deleted_message: bool = self.message_repository.delete_message_by_message_id_and_sender_email(
            self.saved_message.get_message_id(), self.message.get_sender_email())
        self.assertTrue(is_deleted_message)
        self.assertEqual(0, self.message_repository.get_count_of_all_messages())
        self.assertEqual(0, self.message_repository.get_count_of_all_messages_per_user_by_user_id(
            self.saved_message.get_user_id()))

    def test_save_message_get_message_by_folder_id_and_message_id(self):
        found_message = self.message_repository.find_message_by_folder_id_and_message_id(self.saved_message.get_folder_id(), self.saved_message.get_message_id())
        self.assertIsNotNone(found_message)
        self.assertEqual(found_message, self.saved_message)

    def test_get_all_messages_saved_in_a_folder_by_folder_id(self):
        message1 = Message()
        message1.set_sender_email("abdl@gmail.com")
        message1.set_recipient_email("weret@gmail.com")
        message1.set_user_id("1234")
        message1.set_folder_id("3456")
        self.message_repository.save_message(message1)
        list_of_messages: List[Message] = [self.message, message1]
        self.assertListEqual(list_of_messages, self.message_repository.get_all_messages_per_folder("3456"))
