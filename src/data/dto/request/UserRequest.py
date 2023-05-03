class User_Request:

    def __init__(self):
        self._user_name: str = ""
        self._email: str = ""
        self._password: str = ""
        self._phone_number: str = ""

    def set_user_name(self, user_name) -> None:
        self._user_name = user_name

    def get_user_name(self) -> str:
        return self._user_name

    def set_email(self, email) -> None:
        self._email = email

    def get_email(self) -> str:
        return self._email

    def set_password(self, password) -> None:
        self._password = password

    def get_password(self) -> str:
        return self._password

    def set_phone_number(self, phone_number) -> None:
        self._phone_number = phone_number

    def get_phone_number(self) -> str:
        return self._phone_number

    def __str__(self):
        return f"""
        User Name: {self.get_user_name()}
        Email: {self.get_email()}
        Password: {self.get_password()}
        Phone number: {self.get_phone_number()}
        """

    def __repr__(self):
        return f"""
        User Name: {self.get_user_name()}
        Email: {self.get_email()}
        Password: {self.get_password()}
        Phone number: {self.get_phone_number()}
        """

