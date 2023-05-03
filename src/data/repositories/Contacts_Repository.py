from abc import ABC, abstractmethod
from typing import List

from data.models.Contacts import Contacts


class Contacts_Repository(ABC):

    @abstractmethod
    def save_contact(self, contact: Contacts) -> Contacts:
        pass

    @abstractmethod
    def find_contact_by_email(self, contact_email: str) -> Contacts | None:
        pass

    @abstractmethod
    def get_all_contacts_of_a_particular_user(self, user_id: str) -> List[Contacts]:
        pass

    @abstractmethod
    def find_contact_by_contact_id_and_user_id(self, contact_id: str, user_id: str) -> Contacts | None:
        pass

    @abstractmethod
    def find_contact_by_contact_email_and_contact_id(self, contact_email: str, contact_id) -> Contacts | None:
        pass

    def find_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> Contacts | None:
        pass

    @abstractmethod
    def delete_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> bool:
        pass

    @abstractmethod
    def delete_contact_by_contact_id_and_user_id(self, contact_email: str, user_id: str) -> bool:
        pass

    @abstractmethod
    def update_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> Contacts:
        pass

    @abstractmethod
    def get_count_of_contacts_belonging_to_a_particular_user(self, user_id) -> int:
        pass

    @abstractmethod
    def get_count_of_all_contacts(self) -> int:
        pass
