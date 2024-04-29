import unittest
from tkinter import Tk, Entry, Frame, Button
from unittest.mock import patch, mock_open
import os

# Import the signup function to be tested
from Signup import button_clicked


class TestSignupFunctionality(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.mail_entry = Entry(self.root)
        self.user_entry = Entry(self.root)
        self.code_entry = Entry(self.root)
        self.success_message = "User account created successfully!"

        # Create a mock 'Accounts.txt' file content for testing
        self.mock_file_content = "test@example.com,testuser,password\n"

    def test_signup_success(self):
        """Test successful signup process"""
        # Set up mock user inputs
        self.mail_entry.insert(0, "newuser@example.com")
        self.user_entry.insert(0, "newuser")
        self.code_entry.insert(0, "newpassword")

        # Patch the built-in 'open' function to return a mock file object
        with patch(
            "builtins.open", mock_open(read_data=self.mock_file_content)
        ) as mock_file:
            with patch("tkinter.messagebox.showwarning") as mock_showwarning:
                button_clicked()

        # Assert that the 'open' function was called to write to file
        mock_file.assert_called_once_with("path/to/Accounts.txt", "a")

        # Assert that no warning message was shown (successful signup)
        mock_showwarning.assert_not_called()

    def test_signup_user_exists(self):
        """Test signup with existing username"""
        # Set up mock user inputs with existing username
        self.mail_entry.insert(0, "existing@example.com")
        self.user_entry.insert(0, "testuser")
        self.code_entry.insert(0, "password123")

        # Patch the built-in 'open' function to return a mock file object
        with patch(
            "builtins.open", mock_open(read_data=self.mock_file_content)
        ) as mock_file:
            with patch("tkinter.messagebox.showwarning") as mock_showwarning:
                button_clicked()

        # Assert that the 'open' function was not called to write to file
        mock_file.assert_not_called()

        # Assert that the correct warning message was shown
        mock_showwarning.assert_called_once_with(
            title="Warning", message="Username already taken, try different username."
        )

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
