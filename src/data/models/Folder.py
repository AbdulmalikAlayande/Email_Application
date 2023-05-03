class Folder:

    def __init__(self):
        self._folder_id: str = ""
        self._folder_name: str = ""
        self._user_id: str = ""
        self._number_of_read_messages: int = 0
        self._number_of_unread_messages: int = 0

    def set_folder_id(self, folder_id: str) -> None:
        self._folder_id = folder_id

    def get_folder_id(self) -> str:
        return self._folder_id

    def set_folder_name(self, folder_name: str) -> None:
        self._folder_name = folder_name

    def get_folder_name(self) -> str:
        return self._folder_name

    def set_user_id(self, user_id: str) -> None:
        self._user_id = user_id

    def get_user_id(self) -> str:
        return self._user_id

    def set_number_of_read_messages(self, number_of_read_messages: int) -> None:
        self._number_of_read_messages = number_of_read_messages

    def get_number_of_read_messages(self) -> int:
        return self._number_of_read_messages

    def set_number_of_unread_messages(self, number_of_unread_messages: int) -> None:
        self._number_of_unread_messages = number_of_unread_messages

    def get_number_of_unread_messages(self) -> int:
        return self._number_of_unread_messages

    # def __repr__(self):
    #     f"""
    #         Folder Id ==> {self._folder_id}
    #         Folder Name ==> {self._folder_name}
    #         User Id ==> {self._user_id}
    #         Number Of Read Messages ==> {self._number_of_read_messages}
    #         Number Of Unread Messages ==> {self._number_of_unread_messages}
    #         """

    def __str__(self):
        f"""
            Folder Id ==> {self._folder_id}
            Folder Name ==> {self._folder_name}
            User Id ==> {self._user_id}
            Number Of Read Messages ==> {self._number_of_read_messages}
            Number Of Unread Messages ==> {self._number_of_unread_messages}
            """
