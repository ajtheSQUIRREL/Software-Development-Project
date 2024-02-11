from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pytz


root = Tk()
root.title("weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

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


# label
label1 = Label(
    root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label1.pack(padx=5, pady=5, side=BOTTOM)
label1.place(x=150, y=400)

label2 = Label(
    root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label2.pack(padx=5, pady=5, side=BOTTOM)
label2.place(x=270, y=400)


label3 = Label(
    root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label3.pack(padx=5, pady=5, side=BOTTOM)
label3.place(x=440, y=400)


label4 = Label(
    root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label4.pack(padx=5, pady=5, side=BOTTOM)
label4.place(x=650, y=400)


root.mainloop()
