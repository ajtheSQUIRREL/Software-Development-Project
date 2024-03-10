from tkinter import *
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable (False, False)
img=PhotoImage(file='login.png')
Label(root, image=img, bg='white'). place (x=50,y=50)
frame=Frame (root, width=350,height=350, bg="white")
frame.place(x=480,y=70)
heading=Label (frame,text='Sign Up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

mail=Entry(frame, width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
mail.place(x=30,y=80)
mail.insert(0, 'E-mail')
Frame (frame, width=295,height=2, bg='black'). place (x=25,y=100)

user=Entry(frame, width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=120)
user.insert(0, 'Username')
Frame (frame, width=295,height=2, bg='black'). place (x=25,y=140)

code=Entry(frame, width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=160)
code.insert(0, 'Password')
Frame (frame, width=295,height=2, bg='black'). place (x=25,y=180)

code2=Entry(frame, width=25, fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
code2.place(x=30,y=200)
code2.insert(0, 'Re Enter Password')
Frame (frame, width=295,height=2, bg='black'). place (x=25,y=220)



Button(frame, width=39, pady=7,text='Sign Up', bg='#57a1f8', fg='white', border=0).place (x=35,y=250) 


root.mainloop()