class Attachments:

    def __init__(self):
        self._attachment_file_name: str = ""
        self._attachment_id: str = ""
        self._file_type: str = ""
        self._file_size: bytes = b''
        self._message_id: str = ""

    def set_attachment_file_name(self, file_name: str) -> None:
        self._attachment_file_name = file_name

    def get_attachment_file_name(self) -> str:
        return self._attachment_file_name

    def set_attachment_id(self, attachment_id: str) -> None:
        self._attachment_id = attachment_id

    def get_attachment_id(self) -> str:
        return self._attachment_id

    def set_file_type(self, file_type: str) -> None:
        self._file_type = file_type

    def get_file_type(self) -> str:
        return self._file_type

    def set_file_size(self, file_size) -> None:
        self._file_size = file_size

    def get_file_size(self) -> bytes:
        return self._file_size

    def set_message_id(self, message_id) -> None:
        self._message_id = message_id

    def get_message_id(self) -> str:
        return self._message_id

