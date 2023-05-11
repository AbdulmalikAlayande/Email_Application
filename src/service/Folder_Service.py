from abc import ABC, abstractmethod

from data.dto.request.Folder_Request import Folder_Request
from data.dto.response.Folder_Response import Folder_Response


class Folder_Service(ABC):
    @abstractmethod
    def update_folder_name(self, folder_request: Folder_Request) -> Folder_Response:
        pass
