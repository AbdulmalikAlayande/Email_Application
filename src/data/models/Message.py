from datetime import datetime


class Message:
    def __init__(self):
        self._message_id: str = ""
        self._user_id: str = ""
        self._folder_id: str = ""
        self._message_body: str = ""
        self._message_content: str = ""
        self._message_subject: str = ""
        self._contact_id: str = ""
        self._recipient_email: str = ""
        self._sender_email: str = ""
        self._date_and_time_sent = datetime
        self._date_and_time_received = datetime

    def set_message_id(self, message_id) -> None:
        self._message_id = message_id

    def get_message_id(self) -> str:
        return self._message_id

    def set_user_id(self, user_id) -> None:
        self._user_id = user_id

    def get_user_id(self) -> str:
        return self._user_id

    def set_folder_id(self, folder_id) -> None:
        self._folder_id = folder_id

    def get_folder_id(self) -> str:
        return self._folder_id

    def set_message_bdy(self, message_body) -> None:
        self._message_body = message_body

    def get_message_body(self) -> str:
        return self._message_body

    def set_message_subject(self, message_subject) -> None:
        self._message_subject = message_subject

    def get_message_subject(self) -> str:
        return self._sender_email

    def set_message_content(self, message_content) -> None:
        self._message_content = message_content

    def get_message_content(self) -> str:
        return self._message_content

    def set_contact_id(self, contact_id) -> None:
        self._contact_id = contact_id

    def get_contact_id(self) -> str:
        return self._contact_id

    def set_recipient_email(self, recipient_email) -> None:
        self._recipient_email = recipient_email

    def get_recipient_email(self) -> str:
        return self._recipient_email

    def set_sender_email(self, sender_email) -> None:
        self._sender_email = sender_email

    def get_sender_email(self) -> str:
        return self._sender_email

    def set_date_and_time_sent(self, date_time) -> None:
        self._date_and_time_sent = date_time

    def get_date_and_time_sent(self):
        return self._date_and_time_sent

    def set_date_and_time_received(self, date_time) -> None:
        self._date_and_time_received = date_time

    def get_date_and_time_received(self):
        return self._date_and_time_received

    def __repr__(self):
        return f"""
                Message Id ==> {self._message_id}
                User Id ==> {self._user_id}
                Folder Id ==> {self._folder_id}
                Message Body ==> {self._message_body}
                Message Content ==> {self._message_content}
                Message Subject ==> {self._message_subject}
                Contact Id ==> {self._contact_id}
                Recipient Email ==> {self._recipient_email}
                Sender Email ==> {self._sender_email}
                Date and Time Sent ==> {self._date_and_time_sent}
                Date and Time Received ==> {self._date_and_time_received}
                """

    def __str__(self):
        return f"""
                Message Id ==> {self._message_id}
                User Id ==> {self._user_id}
                Folder Id ==> {self._folder_id}
                Message Body ==> {self._message_body}
                Message Content ==> {self._message_content}
                Message Subject ==> {self._message_subject}
                Contact Id ==> {self._contact_id}
                Recipient Email ==> {self._recipient_email}
                Sender Email ==> {self._sender_email}
                Date and Time Sent ==> {self._date_and_time_sent}
                Date and Time Received ==> {self._date_and_time_received}
                """
