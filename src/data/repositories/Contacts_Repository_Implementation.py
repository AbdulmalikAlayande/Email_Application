from typing import List

from data.models.Contacts import Contacts
from data.repositories.Contacts_Repository import Contacts_Repository
from utils.Id_Generator import Id_Generator


class Contacts_Repository_Implementation(Contacts_Repository):

    def get_count_of_contacts_belonging_to_a_particular_user(self, user_id) -> int:
        count_of_contacts_belonging_to_the_particular_user = 0
        for contacts in self._list_of_contacts:
            if contacts.get_user_id() == user_id:
                count_of_contacts_belonging_to_the_particular_user += 1
        return count_of_contacts_belonging_to_the_particular_user

    def __init__(self):
        self._list_of_contacts: List[Contacts] = []

    def save_contact(self, contact: Contacts) -> Contacts:
        if self._contact_exists_in_users_list_of_contacts(contact):
            self._save_new_contact(contact)
        return self._updated_existing_contact(contact)

    def _contact_exists_in_users_list_of_contacts(self, contact):
        if contact.get_user_id() == "" and contact not in self._list_of_contacts:
            return True
        return False

    def _save_new_contact(self, contact: Contacts) -> Contacts:
        contact.set_contact_id(self._generated_id())
        print("Contact Id printed is: "+contact.get_contact_id())
        self._list_of_contacts.append(contact)
        return contact

    def _updated_existing_contact(self, contact) -> Contacts:
        return self.find_contact_by_contact_id_and_user_id(contact.get_contact_id(), contact.get_user_id())

    def _generated_id(self) -> str:
        return Id_Generator.generate_id(self._list_of_contacts)

    def get_count_of_all_contacts(self) -> int:
        return len(self._list_of_contacts)

    def find_contact_by_contact_email_and_contact_id(self, contact_email: str, contact_id) -> Contacts | None:
        for contact in self._list_of_contacts:
            if contact.get_contact_email() == contact_email and contact.get_contact_id() == contact_id:
                return contact
        return None

    # todo: this method impl may have issues later because it should be returning a list not an object
    # todo: since a particular contact may belong to plenty users
    def find_contact_by_email(self, contact_email: str) -> Contacts | None:
        for contact in self._list_of_contacts:
            if contact.get_contact_email() == contact_email:
                return contact
        return None

    def get_all_contacts_of_a_particular_user(self, user_id: str) -> List[Contacts]:
        list_of_contacts_belonging_to_the_particular_user: List[Contacts] = []
        for contact in self._list_of_contacts:
            if contact.get_user_id() == user_id:
                list_of_contacts_belonging_to_the_particular_user.append(contact)
        return list_of_contacts_belonging_to_the_particular_user

    def find_contact_by_contact_id_and_user_id(self, contact_id: str, user_id: str) -> Contacts | None:
        for contact in self._list_of_contacts:
            if contact.get_contact_id() == contact_id and contact.get_user_id() == user_id:
                return contact
        return None

    def delete_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> bool:
        found_contact = self.find_contact_by_contact_email_and_user_id(contact_email, user_id)
        if found_contact is not None:
            self._list_of_contacts.remove(found_contact)
            return True
        return False

    # todo: this guy may also have issues, because a particular contact may belong to plenty users
    # todo: and there by deleting contacts belonging to another user
    def delete_contact_by_contact_id_and_user_id(self, contact_id: str, user_id: str) -> bool:
        found_contact = self.find_contact_by_contact_id_and_user_id(contact_id, user_id)
        if found_contact is not None:
            self._list_of_contacts.remove(found_contact)
            return True
        return False

    def update_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> Contacts:
        pass

    def find_contact_by_contact_email_and_user_id(self, contact_email: str, user_id: str) -> Contacts | None:
        for contact in self._list_of_contacts:
            if contact.get_contact_email() == contact_email and contact.get_user_id() == user_id:
                return contact
        return None
