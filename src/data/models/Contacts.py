class Contacts:

    def __init__(self):
        self._contact_id: str = ""
        self._contact_email: str = ""
        self._user_id: str = ""

    def set_contact_id(self, contact_id: str) -> None:
        self._contact_id = contact_id

    def get_contact_id(self) -> str:
        return self._contact_id

    def set_contact_email(self, contact_email: str) -> None:
        self._contact_email = contact_email

    def get_contact_email(self) -> str:
        return self._contact_email

    def set_user_id(self, user_id: str) -> None:
        self._user_id = user_id

    def get_user_id(self) -> str:
        return self._user_id

    def __str__(self):
        return f"Contact Id= {self._contact_id}\n" \
               f"User Id = {self._user_id}\n" \
               f"Contact Email= {self._contact_email}"

    def __repr__(self):
        return f"Contact Id= {self._contact_id}\n" \
               f"User Id = {self._user_id}\n" \
               f"Contact Email= {self._contact_email}"
