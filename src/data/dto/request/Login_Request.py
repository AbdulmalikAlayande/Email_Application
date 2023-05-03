class Login_Request:

    def __init__(self):
        self._phone_number = ""
        self._email = ""
        self._password = ""

    def set_email(self, email: str = None) -> None:
        self._email = email

    def get_email(self) -> str:
        return self._email

    def set_password(self, password: str = None) -> None:
        self._password = password

    def get_password(self) -> str:
        return self._password

    def set_phone_number(self, phone_number: str) -> None:
        self._phone_number = phone_number

    def get_phone_number(self) -> str:
        return self._phone_number
