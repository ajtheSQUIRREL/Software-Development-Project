import customtkinter as ctk
import tkinter.messagebox as tkmb

ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Weather Application")


def signup():

    username = ""
    password = ""
    new_window = ctk.CTkToplevel(app)

    new_window.title("New Window")

    new_window.geometry("350x150")

    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(
            title="Login Successful", message="You have logged in Successfully"
        )
        ctk.CTkLabel(
            new_window, text="GeeksforGeeks is best for learning ANYTHING !!"
        ).pack()
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title="Wrong password", message="Please check your password")
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title="Wrong username", message="Please check your username")
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")


label = ctk.CTkLabel(app, text="Sign Up To Get Access To The Weather Application")

# label.pack(pady=20, expand=True)


frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Sign Up")
label.pack(pady=12, padx=10)


user_name = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_name.pack(pady=12, padx=10)

user_email = ctk.CTkEntry(master=frame, placeholder_text="Email")
user_email.pack(pady=12, padx=10)

user_address = ctk.CTkEntry(master=frame, placeholder_text="Address")
user_address.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)


button = ctk.CTkButton(master=frame, text="Sign UP", command=signup)
button.pack(pady=12, padx=10)


app.mainloop()
