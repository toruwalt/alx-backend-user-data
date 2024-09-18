#!/usr/bin/env python3
""" Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class that authenticates"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to insist on Authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Method to header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """Loose me"""
        return None
