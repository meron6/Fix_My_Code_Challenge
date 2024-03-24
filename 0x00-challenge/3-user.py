#!/usr/bin/python3
"""3. User password
    script that uses User class from previous exercise
    to test
"""

class User():
    """User class definition
    """

    def __init__(self, password: str) -> None:
        """User initialization
        """

        self.password = password

    def is_valid_password(self, pwd: str) -> bool:
        """validate password
        """

        return pwd == self.password

if __name__ == "__main__":
    usr = User("MyPwd")
    print("Test User")
    print("is_valid_password should return True if it's the right password")
    print(usr.is_valid_password("MyPwd"))  # Add this line to test the is_valid_password method
