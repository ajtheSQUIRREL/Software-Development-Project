import unittest
from tkinter import Tk, Entry, Button
import tkinter.messagebox as messagebox
from unittest.mock import patch

# Import the login function to be tested
from Login import button_clicked_in


class TestLoginFunctionality(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.username_entry = Entry(self.root)
        self.password_entry = Entry(self.root)
        self.success_message = "Login successful!"
        self.failure_message = "Invalid credentials."

    def test_successful_login(self):
        """Test successful login with correct credentials"""
        # Set up mock user inputs
        self.username_entry.insert(0, "testuser")
        self.password_entry.insert(0, "password123")

        # Patch the messagebox.showinfo method to assert success message
        with patch.object(messagebox, "showinfo") as mock_showinfo:
            button_clicked_in(self.username_entry, self.password_entry)

        mock_showinfo.assert_called_once_with("Success", self.success_message)

    def test_failed_login_invalid_password(self):
        """Test login with incorrect password"""
        # Set up mock user inputs
        self.username_entry.insert(0, "testuser")
        self.password_entry.insert(0, "wrongpassword")

        # Patch the messagebox.showerror method to assert failure message
        with patch.object(messagebox, "showerror") as mock_showerror:
            button_clicked_in(self.username_entry, self.password_entry)

        mock_showerror.assert_called_once_with("Error", self.failure_message)

    def test_failed_login_invalid_username(self):
        """Test login with invalid username"""
        # Set up mock user inputs
        self.username_entry.insert(0, "unknownuser")
        self.password_entry.insert(0, "password123")

        # Patch the messagebox.showerror method to assert failure message
        with patch.object(messagebox, "showerror") as mock_showerror:
            button_clicked_in(self.username_entry, self.password_entry)

        mock_showerror.assert_called_once_with("Error", self.failure_message)

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
