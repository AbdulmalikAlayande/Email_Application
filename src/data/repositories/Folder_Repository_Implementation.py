from typing import List

from data.models.Folder import Folder
from data.repositories.Folder_Repository import Folder_Repository
from utils.Id_Generator import Id_Generator


class Folder_Repository_Implementation(Folder_Repository):

    def __init__(self):
        self._list_of_folders: List[Folder] = []
        self._count = 10
        self._auto_increment_for_each_id = 10

    def save_folder(self, folder: Folder) -> Folder:
        if not self._folder_already_exists(folder):
            return self._save_new_folder(folder)
        return self._existing_folder(folder)

    def _folder_already_exists(self, folder) -> bool:
        # todo: this thing fit get error later o bro, because you will need to handle the error
        # todo: the assert keyword throws an assertionFailedError, so therefore you will need to handle the error
        assert folder.get_folder_id() is not None
        for each_folder in self._list_of_folders:
            if each_folder.get_folder_id() == folder.get_folder_id():
                return True
        return False

    def _save_new_folder(self, folder):
        self._count += 1
        self._auto_increment_for_each_id += self._count
        folder.set_folder_id(self.generated_Id())
        self._list_of_folders.append(folder)
        return folder

    def _existing_folder(self, folder) -> Folder:
        return self.find_folder_by_folder_id(folder.get_folder_id())

    def get_count_of_all_folders_for_a_particular_user(self, user_id: str) -> int:
        count_of_folders_belonging_to_the_user = 0
        for each_folder in self._list_of_folders:
            if each_folder.get_user_id() == user_id:
                count_of_folders_belonging_to_the_user += 1
        return count_of_folders_belonging_to_the_user

    def generated_Id(self) -> str:
        return f"{Id_Generator.generate_id(self._list_of_folders) + self._count.__str__() + self._auto_increment_for_each_id.__str__()}"

    def get_count_of_all_folders(self) -> int:
        return len(self._list_of_folders)

    def find_folder_by_folder_name_and_user_id(self, folder_name: str, user_id: str) -> Folder | None:
        for folder in self._list_of_folders:
            if folder.get_folder_name() == folder_name and folder.get_user_id() == user_id:
                return folder
        return None

    def find_folder_by_folder_id(self, folder_id: str) -> Folder | None:
        for each_folder in self._list_of_folders:
            if each_folder.get_folder_id() == folder_id:
                return each_folder
        return None

    def get_all_folders_belonging_to_a_particular_user(self, user_id: str) -> List[Folder] | None:
        list_of_folders_belonging_to_the_particular_user: List[Folder] = []
        for folder in self._list_of_folders:
            if folder.get_user_id() == user_id:
                list_of_folders_belonging_to_the_particular_user.append(folder)
        print(list_of_folders_belonging_to_the_particular_user.__str__())
        return list_of_folders_belonging_to_the_particular_user

    def delete_folder_by_folder_id(self, folder_id) -> bool:
        folder_to_be_deleted: Folder = self.find_folder_by_folder_id(folder_id)
        if folder_to_be_deleted is not None:
            self._list_of_folders.remove(folder_to_be_deleted)
            return True
        return False
