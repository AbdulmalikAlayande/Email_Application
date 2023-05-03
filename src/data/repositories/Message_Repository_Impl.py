import random
from typing import List

from data.models.Message import Message
from utils.Alphabet import Alphabet
from data.repositories.Message_Repository import Message_Repository
from utils.Id_Generator import Id_Generator


class Message_Repository_Impl(Message_Repository):

    def __init__(self):
        self._list_of_messages: List[Message] = []

    def save_message(self, message: Message) -> Message:
        if self._message_exists_in_users_list_of_messages(message):
            return self._save_new_message(message)
        return self._updated_existing_message(message)

    def _message_exists_in_users_list_of_messages(self, message):
        if message.get_message_id() == "" and message not in self._list_of_messages:
            return True
        return False

    def _save_new_message(self, message: Message) -> Message:
        message.set_message_id(self._generated_id())
        self._list_of_messages.append(message)
        return message

    def _updated_existing_message(self, message) -> Message:
        return self.find_message_by_message_id(message.get_message_id())

    def _generated_id(self) -> str:
        return Id_Generator.generate_id(self._list_of_messages)

    def find_message_by_message_id(self, message_id) -> Message | None:
        for message in self._list_of_messages:
            if message.get_message_id() == message_id:
                return message
        return None

    def find_message_by_recipient_email_and_message_id(self, recipient_email: str, message_id: str) -> Message | None:
        for message in self._list_of_messages:
            if message.get_message_id() == message_id and message.get_recipient_email() == recipient_email:
                return message
        return None

    def find_message_by_sender_email_and_message_id(self, sender_email: str, message_id: str) -> Message | None:
        for message in self._list_of_messages:
            if message.get_message_id() == message_id and message.get_sender_email() == sender_email:
                return message
        return None

    def get_all_messages(self) -> List[Message]:
        return self._list_of_messages

    def get_all_messages_per_user(self, user_id) -> List[Message]:
        list_of_messages_for_a_particular_user: List[Message] = []
        for message in self._list_of_messages:
            if message.get_user_id() == user_id:
                list_of_messages_for_a_particular_user.append(message)
        return list_of_messages_for_a_particular_user

    def delete_message_by_message_id(self, message_id: str) -> bool:
        found_message = self.find_message_by_message_id(message_id)
        assert found_message is not None
        self._list_of_messages.remove(found_message)
        return True

    def delete_message_by_message_id_and_recipient_email(self, message_id: str, recipient_email) -> bool:
        found_message = self.find_message_by_recipient_email_and_message_id(recipient_email, message_id)
        assert found_message is not None
        self._list_of_messages.remove(found_message)
        return True

    def delete_message_by_message_id_and_sender_email(self, message_id: str, sender_email) -> bool:
        found_message = self.find_message_by_sender_email_and_message_id(sender_email, message_id)
        assert found_message is not None
        self._list_of_messages.remove(found_message)
        return True

    def get_count_of_all_messages_per_user_by_user_id(self, user_id) -> int:
        count_of_messages_belonging_to_the_particular_user = 0
        for message in self._list_of_messages:
            if message.get_user_id() == user_id:
                count_of_messages_belonging_to_the_particular_user += 1
        return count_of_messages_belonging_to_the_particular_user

    def get_count_of_all_messages(self) -> int:
        return len(self._list_of_messages)

    def get_all_messages_per_folder(self, folder_id) -> List[Message]:
        list_of_messages_in_folder: list[Message] = []
        for message in self._list_of_messages:
            if message.get_folder_id() == folder_id:
                list_of_messages_in_folder.append(message)
        return list_of_messages_in_folder

    def find_message_by_folder_id_and_message_id(self, folder_id: str, message_id: str) -> Message | None:
        for message in self._list_of_messages:
            if message.get_folder_id() == folder_id and message.get_message_id() == message_id:
                return message
        return None

    def update_message(self) -> Message:
        pass

    # todo: when the user enters a keyword, it should separate it into list of strings, then it should check if the each
    # todo: string is contained in each message in the list of messages, but the problem is how do i implement that
    # todo: or the method should take a variable length argument(kwargs), and then do something to get the particular message
    # todo: don't forget that if a keyword is contained in more than one message, return a list pf those messages
    # todo: if there is only one message that contains all the messages, then return only that message, so your method is
    # todo: returning a list or a message object
    def search_by_keyword(self, keyword: str) -> List[Message]:
        pass
