from unittest import TestCase

from data.models.Folder import Folder
from data.repositories.Folder_Repository_Implementation import Folder_Repository_Implementation


class Folder_Repository_Test(TestCase):

    def setUp(self) -> None:
        self.folder_repository = Folder_Repository_Implementation()
        self.folder = Folder()
        self.folder.set_folder_name("Inbox")
        self.folder.set_user_id("1234")
        self.folder.set_number_of_read_messages(12)
        self.folder.set_number_of_unread_messages(13)

    def test_save_new_folder_count_of_saved_folders_is_incremented(self):
        self.folder_repository.save_folder(self.folder)
        self.assertEqual(1, self.folder_repository.get_count_of_all_folders())

    def test_save_a_folder_multiple_times_count_does_not_increment(self):
        saved_folder = self.folder_repository.save_folder(self.folder)
        self.folder_repository.save_folder(saved_folder)
        self.assertEqual(1, self.folder_repository.get_count_of_all_folders())
        self.assertEqual(saved_folder, self.folder)

    def test_save_folder_find_folder_by_folder_id(self):
        self.folder_repository.save_folder(self.folder)
        found_folder = self.folder_repository.find_folder_by_folder_id(self.folder.get_folder_id())
        self.assertIsNotNone(found_folder)
        self.assertEqual(found_folder, self.folder)

    def test_save_folder_find_folder_by_folder_name_and_user_id(self):
        self.folder_repository.save_folder(self.folder)
        found_folder = self.folder_repository.find_folder_by_folder_name_and_user_id(self.folder.get_folder_name(), self.folder.get_user_id())
        self.assertIsNotNone(found_folder)
        self.assertEqual(found_folder, self.folder)

    def test_get_all_folders_belonging_to_a_particular_user(self):
        folder2 = Folder()
        folder2.set_folder_name("outbox")
        folder2.set_user_id("1234")
        self.folder_repository.save_folder(self.folder)
        self.folder_repository.save_folder(folder2)
        self.folder_repository.get_all_folders_belonging_to_a_particular_user("1234")
        # list_of_folders_to_compare = [self.folder, folder2]
        # print(f"{self.folder.__str__()}\n============\n{ folder2.__str__()}")
        # self.assertListEqual(list_of_folders_to_compare, self.folder_repository.get_all_folders_belonging_to_a_particular_user("1234"))
