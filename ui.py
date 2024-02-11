from tkinter import *
import tkinter as tk
# from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox

# from timezonefinder import timezone TimezoneFinder
from datetime import datetime

# import requests
import pytz


root = Tk()
root.title("weather App")
root.geometry("900x500+300+200")
root.resizable(True, True)

# Search Box

Search_image = PhotoImage(file="search_image.png")
myimage = Label(image=Search_image)
myimage.place(x=10, y=26)

textfield = tk.Entry(
    root,
    justify="center",
    width=17,
    font=("poppins", 25, "bold"),
    bg="#404040",
    border=0,
    fg="white",
)
textfield.place(x=38, y=47)
textfield.focus()

search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040")
myimage_icon.place(x=392, y=39)

# logo

logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150, y=100)

# Buttom Boxx

frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

root.mainloop()