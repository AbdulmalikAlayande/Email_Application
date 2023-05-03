from typing import List
from unittest import TestCase

from data.models.Contacts import Contacts
from data.repositories.Contacts_Repository_Implementation import Contacts_Repository_Implementation


class TestContacts_Repository_Test(TestCase):

    def setUp(self) -> None:
        self.contact_repository = Contacts_Repository_Implementation()
        self.contact = Contacts()
        self.saved_contact = self.contact_repository.save_contact(self.contact)

    def test_save_new_contact_count_is_incremented_test(self) -> None:
        print(self.contact.__str__())
        self.assertIsNotNone(self.saved_contact.get_contact_id())
        self.assertIsNotNone(self.saved_contact.get_user_id())
        self.assertEqual(1, self.contact_repository.get_count_of_all_contacts())
        self.assertEqual(1, self.contact_repository.get_count_of_contacts_belonging_to_a_particular_user(self.saved_contact.get_user_id()))

    def test_contact_is_saved_multiple_times_id_does_not_change_and_count_does_not_increment(self):
        self.contact_repository.save_contact(self.saved_contact)
        self.assertEqual(1, self.contact_repository.get_count_of_all_contacts())
        self.assertEqual(1, self.contact_repository.get_count_of_contacts_belonging_to_a_particular_user(self.contact.get_user_id()))

    def test_save_contact_find_saved_contact_by_email(self):
        self.saved_contact.set_contact_email("alabdulmalik03@gmail.com")
        found_contact = self.contact_repository.find_contact_by_email(self.saved_contact.get_contact_email())
        print("The found contact is: \n"+found_contact.__str__())
        self.assertIsNotNone(found_contact)
        self.assertIsNotNone(found_contact.get_contact_email())
        self.assertEqual(found_contact, self.saved_contact)

    def test_get_all_contact_belonging_to_a_particular_user(self):
        self.saved_contact.set_user_id("query")
        self.contact_repository.save_contact(self.saved_contact)
        contact1 = Contacts()
        self.contact_repository.save_contact(contact1)
        contact1.set_user_id("query")
        self.assertEqual(2, self.contact_repository.get_count_of_all_contacts())
        self.assertEqual(2, self.contact_repository.get_count_of_contacts_belonging_to_a_particular_user("query"))
        lists_of_contacts_belonging_to_user_with_user_id_query = [self.saved_contact, contact1]
        list_of_contacts_belonging_to_user_with_user_id_query: List[Contacts] = self.contact_repository.get_all_contacts_of_a_particular_user("query")
        print(list_of_contacts_belonging_to_user_with_user_id_query)
        self.assertListEqual(list_of_contacts_belonging_to_user_with_user_id_query, lists_of_contacts_belonging_to_user_with_user_id_query)

    def test_save_contact_find_contact_by_contact_email_and_contact_id(self):
        self.saved_contact.set_contact_email("alabdulmalik03@gmail.com")
        found_contact = self.contact_repository.find_contact_by_contact_email_and_contact_id(self.saved_contact.get_contact_email(),
                                                                                             self.saved_contact.get_contact_id())
        print("The found contact is: \n" + found_contact.__str__())
        self.assertIsNotNone(found_contact)
        self.assertIsNotNone(found_contact.get_contact_email())
        self.assertIsNotNone(found_contact.get_contact_id())
        self.assertEqual(found_contact, self.saved_contact)

    def test_save_new_contact_delete_contact_by_id_and_user_id(self):
        self.saved_contact.set_user_id("query")
        is_deleted_contact = self.contact_repository.delete_contact_by_contact_id_and_user_id(self.saved_contact.get_contact_id(),
                                                                                              self.saved_contact.get_user_id())
        self.assertTrue(is_deleted_contact)
        self.assertEqual(0, self.contact_repository.get_count_of_all_contacts())
        self.assertEqual(0, self.contact_repository.get_count_of_contacts_belonging_to_a_particular_user(self.saved_contact.get_user_id()))

    def test_save_contact_find_contact_by_contact_email_and_user_id(self):
        self.saved_contact.set_contact_email("alabdulmalik03@gmail.com")
        self.saved_contact.set_user_id("query")
        found_contact = self.contact_repository.find_contact_by_contact_email_and_user_id(self.saved_contact.get_contact_email(), self.saved_contact.get_user_id())
        print("The found contact is: \n" + found_contact.__str__())
        self.assertIsNotNone(found_contact)
        self.assertIsNotNone(found_contact.get_contact_email())
        self.assertIsNotNone(found_contact.get_contact_id())
        self.assertEqual(found_contact, self.saved_contact)
