#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth
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
