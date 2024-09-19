# 0x02. Session Authentication

## Description

This directory contains tasks and projects related to implementing **Session Authentication** in web applications. Session Authentication is a method of verifying the identity of users by storing their authentication state (session) on the server-side. The session ID is often shared with the client, usually in the form of a cookie, allowing for persistent authentication during a session.

The primary goal of the tasks here is to understand how session-based authentication works and how to implement it in a backend system, managing login, logout, and session data.

## Learning Objectives

By completing the tasks in this directory, you will be able to:

- Understand the basic concepts of session-based authentication.
- Implement session-based authentication mechanisms.
- Manage user login and logout functionalities.
- Store and retrieve session data on the server side.
- Handle session expiration and session management.
- Work with cookies and session IDs for state management.

## Key Concepts

- **Session**: A period during which the user interacts with the web application after being authenticated.
- **Session ID**: A unique identifier that is stored on the server and shared with the client (usually through cookies) to track the user's session.
- **Session Expiration**: Sessions are typically temporary and may expire after a certain period of inactivity or after the user logs out.

## Files

Here’s a breakdown of the files and directories within `0x02-Session_authentication`:

- **`auth.py`**: Contains the logic for creating and managing session authentication.
- **`session_auth.py`**: Handles session storage and management, including creating new sessions and invalidating existing ones.
- **`session_db_auth.py`**: An extension of `session_auth.py` to handle session data storage in a database.
- **`views/`**: Contains view functions that interact with session-based authentication, such as login and logout views.
- **`models/`**: Defines the user model and session data structures.

## Requirements

- **Python 3.7+** or higher.
- Libraries used (install via `pip` if necessary):
  - `Flask` (for web framework)
  - `SQLAlchemy` or `SQLite` (for session data storage)
  - `Werkzeug` (for password hashing and security)

## Note

In the industry, you should not implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). This is for the learning purpose, so as to walk through each step of this mechanism to understand session authentication by doing/building it.
