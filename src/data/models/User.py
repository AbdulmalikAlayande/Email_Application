class User:

    def __init__(self):
        self._user_id: str = ""
        self._user_name: str = ""
        self._email: str = ""
        self._password: str = ""
        self._phone_number: str = ""

    def set_user_id(self, user_id: str) -> None:
        self._user_id = user_id

    def get_user_id(self) -> str:
        return self._user_id

    def set_user_name(self, user_name: str) -> None:
        self._user_name = user_name

    def get_user_name(self) -> str:
        return self._user_name

    def set_email(self, email: str) -> None:
        self._email = email

    def get_email(self) -> str:
        return self._email

    def set_password(self, password: str) -> None:
        self._password = password

    def get_password(self) -> str:
        return self._password

    def set_phone_number(self, phone_number: str) -> None:
        self._phone_number = phone_number

    def get_phone_number(self) -> str:
        return self._phone_number

    def __str__(self):
        return f"""
        User Name: {self.get_user_name()}
        User Id: {self.get_user_id()}
        Email: {self.get_email()}
        Password: {self.get_password()}
        Phone number: {self.get_phone_number()}
        """

    def __repr__(self):
        return f"""
        User Name: {self.get_user_name()}
        User Id: {self.get_user_id()}
        Email: {self.get_email()}
        Password: {self.get_password()}
        Phone number: {self.get_phone_number()}
        """
