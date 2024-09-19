#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Class that authenticates"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        """
        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header doesn’t start by Basic (with a space at the end)
        Otherwise, return the value after Basic (after the space)
        You can assume authorization_header contains only one Basic
        
        """

        if authorization_header:
            if isinstance(authorization_header, str):
                if authorization_header.startswith('Basic '):
                    return authorization_header.removeprefix('Basic ')
                return None
            return None
        return None