from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

#window creation
root = Tk()
root.title('Login Page')
root.geometry('600x420+300+200')
root.configure(bg='black')
root.resizable(False,False)

def forget():
    root.destroy()
    import Forget

def signup_page():
    root.destroy()
    import SignUp

def login():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('Error', 'Please enter both Username and Password')
    else:
        try:
            conn = sqlite3.connect('Student_Record.db')
            c = conn.cursor()
            c.execute("SELECT * FROM User_Data WHERE Username=? and Password=?",
                      (username.get(), password.get()))
            row = c.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                messagebox.showinfo('Success', 'You are now logged in')
                root.destroy()
                import HomePage
        except:
            messagebox.showerror('Error', 'Database Connectivity Error')



#image inserting
file = "/Users/suyog/Desktop/Comp IA/Images/Logo1.jpg"
original_image = Image.open(file)
resized_image = original_image.resize((270,270))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root,image=img, borderwidth=0, highlightthickness=0)
image_label.place(x=25, y=70)


#heading


heading = Label(text='Shree Manohar Secondary School',fg='#57a1f8',bg='black',font=('Comic Sans MS',30,'bold'))
heading.place(x=50, y=5)

heading = Label(root,text='Please Login',fg='#57a1f8',bg='black',font=('Comic Sans MS',20,'bold'))
heading.place(x=330, y=70)


#username entry
def enter(e):
    username.delete(0, 'end')

def leave(e):
    name=username.get()
    if name=='':
        username.insert(0, 'Username')

username = Entry(root,width=15,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
username.place(x=330, y=120)
username.insert(0,'Username')
username.bind('<FocusIn>', enter)
username.bind('<FocusOut>',leave)

Frame(root,width=200,height=2,bg='#57a1f8').place(x=330, y=140)


#password entry
def enter(e):
    password.delete(0, 'end')

def leave(e):
    name=password.get()
    if name=='':
        password.insert(0, 'Password')

password = Entry(root,width=15,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
password.place(x=330, y=175)
password.insert(0,'Password')
password.bind('<FocusIn>', enter)
password.bind('<FocusOut>',leave)

Frame(root,width=200,height=2,bg='#57a1f8').place(x=330, y=195)


#Button
custom_theme = ttk.Style()
custom_theme.theme_create('custom_theme', parent='alt',
                          settings={'Login.TButton': {'configure': {'background': '#57a1f8',
                                                              'font': ('Comic Sans MS',12,'bold'),
                                                              'anchor': 'center',
                                                              'borderwidth': 2,
                                                              'relief': RIDGE}}})
custom_theme.theme_use('custom_theme')


login_button = ttk.Button(root,width=24,padding=2,text='Login',command=login, style="Login.TButton")
login_button.place(x=330,y=220)

signup_button = ttk.Button(root,text='Create New Account', width=24, padding=2, style='Login.TButton', command=signup_page)
signup_button.place(x=330,y=290)

custom_theme.configure('Custom.TButton', background='black', foreground='#57a1f8', font=('Comic Sans MS',14,'bold'))

forget_button = ttk.Button(root,width=24,text='Forgot Your Password?', style='Custom.TButton', command=forget)
forget_button.place(x=330,y=325)

heading = Label(root,text="------ OR ------",fg='#57a1f8',bg='black',font=('Comic Sans MS',20,'bold'))
heading.place(x=330, y=250)

#heading = Label(root,text="Student Registration System",fg='#57a1f8',bg='black',font=('Comic Sans MS',23,'bold'))
#heading.place(x=120, y=370)






root.mainloop()

