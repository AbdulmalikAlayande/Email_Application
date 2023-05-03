from _py_abc import ABCMeta
from abc import ABCMeta, abstractmethod
from typing import List

from data.models.Folder import Folder


class Folder_Repository(metaclass=ABCMeta):

    @abstractmethod
    def save_folder(self, folder: Folder) -> Folder:
        pass

    @abstractmethod
    def get_count_of_all_folders(self) -> int:
        pass

    @abstractmethod
    def get_count_of_all_folders_for_a_particular_user(self, user_id: str) -> int:
        pass

    @abstractmethod
    def find_folder_by_folder_name_and_user_id(self, folder_name: str, user_id: str) -> Folder | None:
        pass

    @abstractmethod
    def find_folder_by_folder_id(self, folder_id: str) -> Folder | None:
        pass

    @abstractmethod
    def get_all_folders_belonging_to_a_particular_user(self, user_id: str) -> List[Folder]:
        pass

    @abstractmethod
    def delete_folder_by_folder_id(self, folder_id) -> bool:
        pass

    @abstractmethod
    def update_folder_name(self, folder_id, folder_new_name) -> Folder | None:
        pass
