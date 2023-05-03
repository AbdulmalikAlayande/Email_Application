from abc import abstractmethod, ABCMeta
from typing import List

from data.models.Message import Message


class Message_Repository(metaclass=ABCMeta):

    @abstractmethod
    def save_message(self, message: Message) -> Message:
        pass

    @abstractmethod
    def find_message_by_message_id(self, message_id: str) -> Message | None:
        pass

    @abstractmethod
    def find_message_by_recipient_email_and_message_id(self, recipient_email: str, message_id: str) -> Message | None:
        pass

    @abstractmethod
    def find_message_by_sender_email_and_message_id(self, sender_email: str, message_id: str) -> Message:
        pass

    @abstractmethod
    def get_all_messages(self) -> List[Message]:
        pass

    @abstractmethod
    def get_all_messages_per_user(self, user_id) -> List[Message]:
        pass

    @abstractmethod
    def get_all_messages_per_folder(self, folder_id) -> List[Message]:
        pass

    @abstractmethod
    def find_message_by_folder_id_and_message_id(self, folder_id: str, message_id: str) -> Message | None:
        pass

    @abstractmethod
    def update_message(self) -> Message:
        pass

    @abstractmethod
    def delete_message_by_message_id(self, message_id: str) -> bool:
        pass

    @abstractmethod
    def delete_message_by_message_id_and_recipient_email(self, message_id: str, recipient_email) -> bool:
        pass

    @abstractmethod
    def delete_message_by_message_id_and_sender_email(self, message_id: str, sender_email) -> bool:
        pass

    @abstractmethod
    def search_by_keyword(self, keyword: str) -> List[Message]:
        pass

    @abstractmethod
    def get_count_of_all_messages_per_user_by_user_id(self, user_id) -> int:
        pass

    @abstractmethod
    def get_count_of_all_messages(self) -> int:
        pass
