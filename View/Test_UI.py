import unittest
import tkinter as tk
from tkinter import Entry, Button
from tkinter.test import simulate
from client import getWeather

class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.title("Test Weather App")
        self.entry = Entry(self.root)
        self.entry.pack()
        self.search_button = Button(self.root, text="Search", command=getWeather)
        self.search_button.pack()

    def tearDown(self):
        self.root.destroy()

    def test_search_button_click(self):
        # Simulate entering a city name in the entry field
        self.entry.insert(0, "New York")
        # Simulate clicking the search button
        simulate.mouse_click(self.search_button)
        # Add assertions here to verify the expected behavior after clicking the search button
        # For example, you can check if the weather information is displayed correctly in the GUI

if __name__ == "__main__":
    unittest.main()
