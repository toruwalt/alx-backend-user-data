#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth


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
