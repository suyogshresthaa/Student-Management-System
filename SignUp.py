from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

def clear():
    user_entry.delete(0, END)
    password_entry.delete(0, END)
    repassword_entry.delete(0, END)


def sign_up():
    if user_entry.get() =='' or password_entry.get() =='' or repassword_entry.get() =='':
        messagebox.showerror('Invalid', 'All fields are required')

    elif password_entry.get() != repassword_entry.get():
        messagebox.showerror('Error', 'Passwords do not match')

    else:
        try:
            conn = sqlite3.connect('Student_Record.db')
            c = conn.cursor()
            c.execute("SELECT * FROM User_Data WHERE Username=?",
                      (user_entry.get(),))
            row = c.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Username Already Exists')
            else:
                c.execute("INSERT INTO User_Data VALUES(?,?)",
                          (user_entry.get(), password_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'You are registered successfully')
                clear()
                root.destroy()
                import LoginPage
        except:
            messagebox.showerror('Error', "Database Connectivity Issue")
            return


def login_page():
    root.destroy()
    import LoginPage

#window creation
root = Tk()
root.title('Student Registration System')
root.geometry('700x400+300+200')
root.configure(bg='black')
root.resizable(False,False)

#image inserting
file = "/Users/suyog/Desktop/Comp IA/Images/Logo1.jpg"
original_image = Image.open(file)
resized_image = original_image.resize((300,300))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root,image=img, borderwidth=0, highlightthickness=0)
image_label.place(x=40, y=70)

heading = Label(text='Shree Manohar Secondary School',fg='#57a1f8',bg='black',font=('Comic Sans MS',30))
heading.place(x=90, y=5)

heading = Label(root,text='Create An Account',fg='#57a1f8',bg='black',font=('Comic Sans MS',23,'bold'))
heading.place(x=380, y=60)


### LABELS ######
user_label = Label(root,text='Username: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
user_label.place(x=380, y=110)
user_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
user_entry.place(x=380, y=140)
user_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
user_line.place(x=380, y=160)

password_label = Label(root,text='Password: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
password_label.place(x=380, y=170)
password_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
password_entry.place(x=380, y=200)
password_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
password_line.place(x=380, y=220)

repassword_label = Label(root,text='Re-Enter Password: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
repassword_label.place(x=380, y=230)
repassword_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
repassword_entry.place(x=380, y=260)
repassword_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
repassword_line.place(x=380, y=280)

### BUTTONS #####
custom_theme = ttk.Style()
custom_theme.theme_create('custom_theme', parent='alt',
                          settings={'Login.TButton': {'configure': {'background': '#57a1f8',
                                                              'font': ('Comic Sans MS',12,'bold'),
                                                              'anchor': 'center',
                                                              'borderwidth': 2,
                                                              'relief': RIDGE}}})
custom_theme.theme_use('custom_theme')


signup_button = ttk.Button(root,width=18,padding=2,text='Sign Up', style="Login.TButton", command=sign_up)
signup_button.place(x=380,y=300)


alracc = Label(root,text="Already have an account?",fg='#57a1f8',bg='black',font=('Comic Sans MS',14,'bold'))
alracc.place(x=380, y=340)

custom_theme.configure('Custom.TButton', background='black', foreground='#57a1f8', font=('Comic Sans MS',16,'bold'))

login_button = ttk.Button(root,width=24,text='Log In', style='Custom.TButton',command=login_page)
login_button.place(x=560,y=338)

root.mainloop()
