from typing import Optional

from schema import Schema  # type: ignore

from client.server_comms.base_server_request import BaseServerRequest
from common.client_server_protocols import credential_check_server_schema


class CredentialCheckServerRequest(BaseServerRequest):
    def __init__(self, username: str, password: str) -> None:
        """
        Create server request for credential checking.
        :param username:    the username that the user gives in
        :param password:    the password that the user gives in
        """
        super().__init__()
        self._response_schema: Schema = credential_check_server_schema
        self._send_message.update(
            {
                "protocol_type": self._response_schema.schema["protocol_type"],
                "username": username,
                "password": password,
            }
        )

    def is_response_success(self) -> Optional[bool]:
        """
        Returns whether the response was a success
        :return: True if success, false if failure, None if response is expected but hasn't arrived yet
        """
        if self._response_success is None:
            return None
        elif self._response_success is False:
            return False
        else:
            return self._response_message["success"]

    def get_encrypted_password(self) -> Optional[int]:
        """
        Retrieves encrypted password from the server response if available
        :return: Encrypted password if available, None otherwise
        """
        if self.is_response_success() is True:
            return self._response_message["encrypted_password"]
        else:
            return None

    def get_account_id(self) -> Optional[int]:
        """
        Retrieves account ID from the server response if available
        :return: Account ID if available, None otherwise
        """
        if self.is_response_success() is True:
            return self._response_message["account_id"]
        else:
            return None