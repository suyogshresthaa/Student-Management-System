from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import sqlite3

def reset():
    if user_entry.get() =='' or newpassword_entry.get() =='' or conpassword_entry.get() =='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif newpassword_entry.get() != conpassword_entry.get():
        messagebox.showerror('Error', 'Passwords Do Not Match')
    else:
        conn = sqlite3.connect('Student_Record.db')
        c = conn.cursor()
        c.execute("SELECT * FROM User_Data WHERE Username=?",
                  (user_entry.get(),))
        row = c.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Username is Incorrect')
        else:
            c.execute("UPDATE User_Data SET Password=? WHERE Username=?",
                      (newpassword_entry.get(), user_entry.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success', 'Password has been changed. Please login with new password.')
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
resized_image = original_image.resize((270,270))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root,image=img, borderwidth=0, highlightthickness=0)
image_label.place(x=50, y=50)

heading = Label(text='Shree Manohar Secondary School',fg='#57a1f8',bg='black',font=('Comic Sans MS',30))
heading.place(x=90, y=5)

heading = Label(root,text='Reset Your Password',fg='#57a1f8',bg='black',font=('Comic Sans MS',23,'bold'))
heading.place(x=380, y=60)


### LABELS ######
user_label = Label(root,text='Username: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
user_label.place(x=380, y=110)
user_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
user_entry.place(x=380, y=140)
user_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
user_line.place(x=380, y=160)

newpassword_label = Label(root,text='New Password: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
newpassword_label.place(x=380, y=170)
newpassword_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
newpassword_entry.place(x=380, y=200)
newpassword_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
newpassword_line.place(x=380, y=220)

conpassword_label = Label(root,text='Confirm Password: ',fg='#57a1f8',bg='black',font=('Comic Sans MS',16,'bold'))
conpassword_label.place(x=380, y=230)
conpassword_entry = Entry(root,width=25,fg='white',bg='black',border=0,font=('Arial',14), highlightthickness=0)
conpassword_entry.place(x=380, y=260)
conpassword_line = Canvas(root, highlightthickness=0, bg='#57a1f8', width=230, height=1.5)
conpassword_line.place(x=380, y=280)

### BUTTONS #####
custom_theme = ttk.Style()
custom_theme.theme_create('custom_theme', parent='alt',
                          settings={'Login.TButton': {'configure': {'background': '#57a1f8',
                                                              'font': ('Comic Sans MS',14,'bold'),
                                                              'anchor': 'center',
                                                              'borderwidth': 2,
                                                              'relief': RIDGE}}})
custom_theme.theme_use('custom_theme')


reset_button = ttk.Button(root,width=18,padding=2,text='Reset', style="Login.TButton", command=reset)
reset_button.place(x=380,y=300)


root.mainloop()
