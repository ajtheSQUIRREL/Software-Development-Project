from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pytz
from geopy import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import random
import sys

sys.path.insert(
    1,
    "E://Study//3-1//Software Development Project//Weather Application//DEV//Software-Development-Project//Controller",
)
import Logic

global textfield, Nominatim, TimezoneFinder, datetime, pytz, clock, name, server
if __name__ == "__main__":

    root = Tk()
    root.title("weather App")
    root.geometry("900x500+300+200")
    root.resizable(False, False)

    def getWeather():
        city = textfield.get()

        geolocation = Nominatim(user_agent="GetLoc")
        location = geolocation.geocode(city, timeout=None)
        obj = TimezoneFinder()
        Latitude = location.latitude
        Longitude = location.longitude
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")

        clock.config(text=current_time)
        name.config(text="CURRENT TIME")
        info = Logic.weather_data(city)
        print(info)
        temp = info["Temperature"]
        Description = info["Condition"]
        wind = info["wind"]
        Humidity = info["Humidity"]
        Pressure = info["pressure"]
        # weather
        t.config(text=(temp, "°"))
        c.config(text=(Description, "|", "FEELS", "Like", temp, "°"))

        w.config(text=wind)
        h.config(text=Humidity)
        d.config(text=Description)
        p.config(text=Pressure)

        forecast_heading = Label(
            root,
            text="7-Day Forecast",
            font=("Helvetica", 15, "bold"),
            fg="white",
            bg="#1ab5ef",
        )
        forecast_heading.place(x=720, y=50)

        # Forecast labels
        forecast_labels = []
        for i in range(7):
            forecast_label = Label(
                root,
                text=f"Day {i+1} : {round(random.uniform(temp-5,temp+5),2)} ",
                font=("arial", 15, "bold"),
                bg="#1ab5ef",
            )
            forecast_label.place(x=730, y=100 + i * 30)
            forecast_labels.append(forecast_label)

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
    myimage_icon = Button(
        image=search_icon,
        borderwidth=0,
        cursor="hand2",
        bg="#404040",
        command=getWeather,
    )
    myimage_icon.place(x=392, y=39)

    # logo

    logo_image = PhotoImage(file="logo.png")
    logo = Label(image=logo_image)
    logo.place(x=150, y=100)

    # time

    name = Label(
        root,
        font=("arial", 15, "bold"),
    )
    name.place(x=30, y=100)
    clock = Label(
        root,
        font=(
            "Helvetica",
            15,
        ),
    )
    clock.place(x=30, y=130)

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
        root,
        text="DESCRIPTION",
        font=("Helvetica", 15, "bold"),
        fg="white",
        bg="#1ab5ef",
    )
    label3.pack(padx=5, pady=5, side=BOTTOM)
    label3.place(x=440, y=400)

    label4 = Label(
        root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
    )
    label4.pack(padx=5, pady=5, side=BOTTOM)
    label4.place(x=650, y=400)

    t = Label(font=("arial", 70, "bold"), fg="#ee666d")
    t.place(x=400, y=150)
    c = Label(font=("arial", 15, "bold"))
    c.place(x=400, y=250)

    w = Label(text="... ", font=("arial", 15, "bold"), bg="#1ab5ef")
    w.place(x=160, y=430)

    h = Label(text="... ", font=("arial", 15, "bold"), bg="#1ab5ef")
    h.place(x=300, y=430)

    d = Label(text="... ", font=("arial", 15, "bold"), bg="#1ab5ef")
    d.place(x=490, y=430)

    p = Label(text="... ", font=("arial", 15, "bold"), bg="#1ab5ef")
    p.place(x=700, y=430)

    root.mainloop()
