from tkinter import *
import tkinter.messagebox


def button_clicked_up():
    root.destroy()
    with open("Signup.py") as app:
        exec(app.read())


def button_clicked_in():
    u = user.get()
    password = code.get()
    # print(u, password)
    file = open(
        "E://Study//3-1//Software Development Project//Weather Application//DEV//Software-Development-Project//Model//Accounts.txt",
        "r",
    )
    lines = file.readlines()
    flag = 0
    for l in lines:
        m2, u2, pass2 = l.split(",")
        print(m2, u2, pass2)
        if u == u2:
            password = password + "\n"
            if password != pass2:
                print(pass2)
                print(password)
                tkinter.messagebox.showwarning(
                    title=Warning, message="Incorrect Password"
                )
                flag = 2
                break
            if password == pass2:
                flag = 1
                break
    if flag == 0:
        tkinter.messagebox.showwarning(title=Warning, message="User Does not exist")
    file.close()
    if flag == 1:
        root.destroy()
        with open("UI.py") as app:
            exec(app.read())


root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)
img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)
heading = Label(
    frame,
    text="Sign in",
    fg="#57a1f8",
    bg="white",
    font=("Microsoft YaHei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)

user = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
user.place(x=30, y=80)
user.insert(0, "Username")
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

code = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft YaHei UI Light", 11),
)
code.place(x=30, y=150)
code.insert(0, "Password")
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


Button(
    frame,
    width=39,
    pady=7,
    text="Sign in",
    bg="#57a1f8",
    fg="white",
    border=0,
    command=button_clicked_in,
).place(x=35, y=204)
label = Label(
    frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("Microsoft YaHei UI Light", 9),
)
label.place(x=75, y=270)
sign_up = Button(
    frame,
    width=6,
    text="Sign up",
    border=0,
    bg="white",
    cursor="hand2",
    fg="#57a1f8",
    command=button_clicked_up,
)
sign_up.place(x=215, y=270)


root.mainloop()
