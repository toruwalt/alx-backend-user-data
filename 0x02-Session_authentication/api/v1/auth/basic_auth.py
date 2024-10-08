#!/usr/bin/env python3
"""Basic Auth Module"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """Class that authenticates"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header:
            if isinstance(authorization_header, str):
                if authorization_header.startswith('Basic '):
                    return authorization_header.removeprefix('Basic ')
                return None
            return None
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    decoded_bytes = base64.b64decode(
                        base64_authorization_header)
                    decoded_string = decoded_bytes.decode('utf-8')
                    return decoded_string
                except Exception as e:
                    return None
            return None
        return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):  # type: ignore
        """returns the user email and password
        from the Base64 decoded value.
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if decoded_base64_authorization_header.__contains__(':'):
                    return decoded_base64_authorization_header.split(':')
                return None, None
            return None, None
        return None, None

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd:
                                     str) -> TypeVar('User'):  # type: ignore
        """Returns email and password"""
        if user_email and isinstance(user_email, str):
            if user_pwd and isinstance(user_pwd, str):
                try:
                    users = User.search({'email': user_email})
                    if users:
                        if users[0].is_valid_password(user_pwd):
                            return users[0]
                    return None
                except Exception as e:
                    return None
            return None
        return None
