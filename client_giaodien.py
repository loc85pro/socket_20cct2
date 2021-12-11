from tkinter import *
from tkinter import Tk
import tkinter

window=Tk()
window.geometry("1280x720")
login_screen_photo=PhotoImage(file="login_screen.png")
register_screen_photo=PhotoImage(file="register_screen.png")


def print_username_password(username, password):
    print(username)
    print(password)

def register_screen():
    register_window=Toplevel()
    register_window.geometry("1280x720")
    global register_screen_photo
    #add ảnh vào cửa sổ
    Label(register_window, image=register_screen_photo, bg="black").place(x=0, y=0)
    
    #tạo 2 cái text box username với password
    username_tb=Entry(register_window, text="enter your username", bg="white", fg="black", font=("Roboto", 24), bd=0, width=26)
    username_tb.place(x=426, y=313)
    password_tb=Entry(register_window, text="enter your password", bg="white", fg="black", font=("Roboto", 24), bd=0, width=26)
    password_tb.place(x=426, y=460)
    
    #tạo button NEXT
    next_button=Button( register_window, text="Next",fg="white", font=("Roboto", 11, "bold"), bd=0, bg="#1a73e8", height=2, width=11, command=lambda: print_username_password(username_tb.get(), password_tb.get())).place(x=809,y=580)
    
def login_screen():
    global window
    global login_screen_photo
    #add ảnh vào cửa sổ
    login_screen_photo=PhotoImage(file="login_screen.png")
    Label(window, image=login_screen_photo, bg="black").place(x=0, y=0)
    
    #tạo 2 cái text box username với password
    username_tb=Entry(window, text="enter your username", bg="white", fg="black", font=("Roboto", 24), bd=0, width=26)
    username_tb.place(x=426, y=313)
    password_tb=Entry(window, text="enter your password", bg="white", fg="black", font=("Roboto", 24), bd=0, width=26)
    password_tb.place(x=426, y=460)
    
    #tạo button NEXT
    next_button=Button( window, text="Next",fg="white", font=("Roboto", 11, "bold"), bd=0, bg="#1a73e8", height=2, width=11, command=lambda: print_username_password(username_tb.get(), password_tb.get())).place(x=809,y=580)
    
    #tạo button Create Account
    create_account_button=Button(window, text="Create Account",fg="#1a73e8", font=("Roboto", 12, "bold"), bd=0, bg="white", height=3, width=16, command=register_screen).place(x=401,y=570)


login_screen()
mainloop()
