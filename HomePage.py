from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox


#window creation
root = Tk()
root.title('Student Registration System')
root.geometry('700x400+300+200')
root.configure(bg='black')
root.resizable(False,False)

def back():
    quit = messagebox.askyesno("Exit", "Do you want to exit?", parent=root)
    if quit == True:
        root.destroy()

def add():
    root.withdraw()
    import Add_Std

def manage():
    root.withdraw()
    import Manage_std

def view():
    root.withdraw()
    import View_Std

############# IMAGE #############
file = "/Users/suyog/Desktop/Comp IA/Images/Logo1.jpg"
original_image = Image.open(file)
resized_image = original_image.resize((270,270))
img = ImageTk.PhotoImage(resized_image)
image_label = Label(root,image=img, borderwidth=0, highlightthickness=0)
image_label.place(x=50, y=70)


############# Color theme #############
custom_theme = ttk.Style()
custom_theme.theme_create('custom_theme', parent='alt',
                          settings={'TButton': {'configure': {'background': '#57a1f8',
                                                              'font': ('Comic Sans MS',12,'bold'),
                                                              'anchor': 'center',
                                                              'borderwidth': 4,
                                                              'relief': RIDGE}}})
custom_theme.theme_use('custom_theme')


############# HEADINGS #############
frame = Frame(root,width=300,height=255,bg='black')
frame.place(x=350, y=70)

heading = Label(text='Welcome to Student Registration System',fg='#57a1f8',bg='black',font=('Comic Sans MS',30))
heading.place(x=50, y=5)

heading = Label(frame,text='Please choose an action',fg='#57a1f8',bg='black',font=('Comic Sans MS',17))
heading.place(x=50, y=0)


############# BUTTONS #############
back_button = ttk.Button(frame,width=20,padding=2,text='Exit Application',command=back)
back_button.place(x=60,y=220)
add_button = ttk.Button(frame,width=20,padding=2,text='Add Students Records',command=add)
add_button.place(x=60,y=110)
manage_button = ttk.Button(frame,width=20,padding=2,text='Manage Students Records',command=manage)
manage_button.place(x=60,y=165)
view_button = ttk.Button(frame,width=20,padding=2,text='View Students Records',command=view)
view_button.place(x=60,y=55)


root.mainloop()

