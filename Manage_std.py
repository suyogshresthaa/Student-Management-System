from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3
from tkinter import ttk
from ttkthemes import themed_tk as tk

#window creation
class Manage_std:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")
        self.root.geometry('1366x768')
        self.root.configure(bg='black')

        title = Label(self.root,text='Manage Student Registrations ',font=('Comic Sans MS',40),border=5,relief=RIDGE,fg='black',bg='#57a1f8')
        title.pack(fill=X)

        ##################################################################
        ###################### Variables ##############################
        ##################################################################

        self.FirstName = StringVar()
        self.Surname = StringVar()
        self.MiddleName = StringVar()
        self.BirthDate = StringVar()
        self.StudentID = StringVar()
        self.YearLevel = StringVar()
        self.StudentNum = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Email = StringVar()
        self.MotherName = StringVar()
        self.FatherName = StringVar()
        self.MotherOcc = StringVar()
        self.FatherOcc = StringVar()
        self.FatherNum = StringVar()
        self.MotherNum = StringVar()
        self.FunderName = StringVar()
        self.FunderNum = StringVar()
        self.EmeName = StringVar()
        self.EmeRelation = StringVar()
        self.EmeNum = StringVar()


        ##################################################################
        ###################### Info Frame##############################
        ##################################################################

        info_frame = Frame(self.root, width=380, height=670, bg='#57a1f8', border=5, relief=RIDGE)
        info_frame.place(x=960, y=80)

        info_title = Label(info_frame, text="Manage Students", font=('Comic Sans MS', 16, 'bold'), fg='black',
                        bg='#57a1f8')
        info_title.place(x=90, y=0)

        # ------------------------- First Name ---------------------------
        fname_label = Label(info_frame, text='First Name: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        fname_label.place(x=0, y=30)

        fname_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.FirstName)
        fname_entry.place(x=90, y=30, width=250)

        fname_line = Canvas(info_frame, highlightthickness=0, bg='black', width=250, height=1.5)
        fname_line.place(x=90, y=50)

        # ------------------------- SurName ---------------------------
        sname_label = Label(info_frame, text='Surname: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        sname_label.place(x=0, y=55)

        sname_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.Surname)
        sname_entry.place(x=75, y=55, width=265)

        sname_line = Canvas(info_frame, highlightthickness=0, bg='black', width=265, height=1.5)
        sname_line.place(x=75, y=75)

        # ------------------------- Middle Name ---------------------------
        mname_label = Label(info_frame, text='Middle Name (If Any): ', bg='#57a1f8', fg='black', font=('Arial', 16))
        mname_label.place(x=0, y=80)

        mname_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.MiddleName)
        mname_entry.place(x=162, y=80, width=180)

        mname_line = Canvas(info_frame, highlightthickness=0, bg='black', width=180, height=1.5)
        mname_line.place(x=162, y=100)

        # ------------------------- Birth ---------------------------
        self.birth_label = Label(info_frame, text='Birth Date: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        self.birth_label.place(x=0, y=105)

        self.birth_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                 font=('Arial', 15), textvariable=self.BirthDate)
        self.birth_entry.place(x=85, y=105, width=258)
        self.birth_entry.insert(0, 'dd/mm/yyyy')
        self.birth_entry.bind('<1>', self.pick_date)

        self.birth_line = Canvas(info_frame, highlightthickness=0, bg='black', width=258, height=1.5)
        self.birth_line.place(x=85, y=125)

        # ------------------------- Student ID ---------------------------
        sID_label = Label(info_frame, text='Student ID: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        sID_label.place(x=0, y=130)

        sID_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                          font=('Arial', 15), textvariable=self.StudentID)
        sID_entry.place(x=90, y=130, width=253)

        sID_line = Canvas(info_frame, highlightthickness=0, bg='black', width=253, height=1.5)
        sID_line.place(x=90, y=150)

        # ------------------------- Class level ---------------------------
        ay_label = Label(info_frame, text='Year Level: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        ay_label.place(x=0, y=155)

        class_combo = ttk.Combobox(info_frame, font=('Arial', 14, 'bold'), state='readonly',
                                   width=30, textvariable=self.YearLevel)

        class_combo['values'] = ['1', '2', '3', '4', '5', '6', '7', '8']
        class_combo.place(x=90, y=155)

        # ------------------------- Student Number ---------------------------
        snumber_label = Label(info_frame, text="Student's Number:", bg='#57a1f8', fg='black', font=('Arial', 16))
        snumber_label.place(x=0, y=175)

        snumber_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.StudentNum)
        snumber_entry.place(x=140, y=175, width=200)

        snumber_line = Canvas(info_frame, highlightthickness=0, bg='black', width=200, height=1.5)
        snumber_line.place(x=140, y=195)

        # ------------------------- Gender ---------------------------
        gen_label = Label(info_frame, text='Gender: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        gen_label.place(x=0, y=200)

        gen_combo = ttk.Combobox(info_frame, font=('Arial', 14, 'bold'), state='readonly',
                                 width=33, textvariable=self.Gender)

        gen_combo['values'] = ['Male', 'Female', 'Other']
        gen_combo.place(x=65, y=200)

        # ------------------------- Full Address ---------------------------
        snumber_label = Label(info_frame, text='Full Address: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        snumber_label.place(x=0, y=225)

        snumber_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.Address)
        snumber_entry.place(x=100, y=225, width=240)

        snumber_line = Canvas(info_frame, highlightthickness=0, bg='black', width=240, height=1.5)
        snumber_line.place(x=100, y=245)

        # ------------------------- Email ---------------------------
        email_label = Label(info_frame, text='Email: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        email_label.place(x=0, y=250)

        email_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.Email)
        email_entry.place(x=50, y=250, width=290)

        email_line = Canvas(info_frame, highlightthickness=0, bg='black', width=290, height=1.5)
        email_line.place(x=50, y=270)

        # ------------------------- Father ---------------------------
        father_label = Label(info_frame, text="Father's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        father_label.place(x=0, y=275)

        father_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.FatherName)
        father_entry.place(x=115, y=275, width=225)

        father_line = Canvas(info_frame, highlightthickness=0, bg='black', width=225, height=1.5)
        father_line.place(x=115, y=295)

        # ------------------------- Father Job ---------------------------
        fatherjob_label = Label(info_frame, text="Father's Occupation: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        fatherjob_label.place(x=0, y=300)

        fatherjob_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.FatherOcc)
        fatherjob_entry.place(x=155, y=300, width=185)

        fatherjob_line = Canvas(info_frame, highlightthickness=0, bg='black', width=185, height=1.5)
        fatherjob_line.place(x=155, y=320)

        # ------------------------- Mother ---------------------------
        mother_label = Label(info_frame, text="Mother's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        mother_label.place(x=0, y=325)

        mother_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.MotherName)
        mother_entry.place(x=120, y=325, width=220)

        mother_line = Canvas(info_frame, highlightthickness=0, bg='black', width=220, height=1.5)
        mother_line.place(x=120, y=345)

        # ------------------------- Mother Job ---------------------------
        motherjob_label = Label(info_frame, text="Mother's Occupation: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        motherjob_label.place(x=0, y=350)

        motherjob_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.MotherOcc)
        motherjob_entry.place(x=160, y=350, width=180)

        motherjob_line = Canvas(info_frame, highlightthickness=0, bg='black', width=180, height=1.5)
        motherjob_line.place(x=160, y=370)

        # ------------------------- Father Number ---------------------------
        fathernum_label = Label(info_frame, text="Father's Number: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        fathernum_label.place(x=0, y=375)

        fathernum_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.FatherNum)
        fathernum_entry.place(x=130, y=375, width=210)

        fathernum_line = Canvas(info_frame, highlightthickness=0, bg='black', width=210, height=1.5)
        fathernum_line.place(x=130, y=395)

        # ------------------------- Mother Number ---------------------------
        motherjob_label = Label(info_frame, text="Mother's Number: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        motherjob_label.place(x=0, y=400)

        motherjob_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.MotherNum)
        motherjob_entry.place(x=135, y=400, width=205)

        motherjob_line = Canvas(info_frame, highlightthickness=0, bg='black', width=205, height=1.5)
        motherjob_line.place(x=135, y=420)

        # ------------------------- Funder Name ---------------------------
        sponame_label = Label(info_frame, text="Funder's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        sponame_label.place(x=0, y=425)

        sponame_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.FunderName)
        sponame_entry.place(x=120, y=425, width=220)

        sponame_line = Canvas(info_frame, highlightthickness=0, bg='black', width=220, height=1.5)
        sponame_line.place(x=120, y=445)

        # ------------------------- Funder Number ---------------------------
        sponum_label = Label(info_frame, text="Funder's Number: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        sponum_label.place(x=0, y=450)

        sponum_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.FunderNum)
        sponum_entry.place(x=135, y=450, width=207)

        sponum_line = Canvas(info_frame, highlightthickness=0, bg='black', width=207, height=1.5)
        sponum_line.place(x=135, y=470)

        # ------------------------- Emergency Name ---------------------------
        emename_label = Label(info_frame, text="Person's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        emename_label.place(x=0, y=475)

        emename_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.EmeName)
        emename_entry.place(x=120, y=475, width=220)

        emename_line = Canvas(info_frame, highlightthickness=0, bg='black', width=220, height=1.5)
        emename_line.place(x=120, y=495)

        # ------------------------- Emergency Number ---------------------------
        emenum_label = Label(info_frame, text="Person's Number: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        emenum_label.place(x=0, y=500)

        emenum_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.EmeNum)
        emenum_entry.place(x=135, y=500, width=207)

        emenum_line = Canvas(info_frame, highlightthickness=0, bg='black', width=207, height=1.5)
        emenum_line.place(x=135, y=520)

        # ------------------------- Emergency Relation ---------------------------
        emerel_label = Label(info_frame, text="Person's Relation to Child: ", bg='#57a1f8', fg='black',
                             font=('Arial', 16))
        emerel_label.place(x=0, y=525)

        emerel_entry = Entry(info_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.EmeRelation)
        emerel_entry.place(x=195, y=525, width=148)

        emerel_line = Canvas(info_frame, highlightthickness=0, bg='black', width=148, height=1.5)
        emerel_line.place(x=195, y=545)

        ##################################################################
        ###################### Record Frame##############################
        ##################################################################

        rcd_frame = Frame(self.root, width=920, height=670, bg='#57a1f8', border=5, relief=RIDGE)
        rcd_frame.place(x=20,y=80)



        # ------------------------- Tree View ---------------------------
        tree_frame = Frame(rcd_frame, width=880, height=630, bg='black', border=7, relief=RIDGE)
        tree_frame.place(x=10, y=10)

        s = ttk.Style(root)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=('Comic Sans MS', 14, "bold"), foreground="black",
                        background="#57a1f8")
        s.configure("TButton", background="#83838B", border=20, relief=RIDGE, font=("Comic Sans MS", 14, "bold"))

        y_scroll = Scrollbar(rcd_frame, orient=VERTICAL)
        x_scroll = Scrollbar(rcd_frame, orient=HORIZONTAL)

        self.tree = ttk.Treeview(tree_frame, columns=(
                "FirstName",
                "Surname",
                "MiddleName",
                "BirthDate",
                "StudentID",
                "Class",
                "StudentNumber",
                "Gender",
                "Address",
                "Email",
                "FatherName",
                "MotherName",
                "FatherJob",
                "MotherJob",
                "FatherNumber",
                "MotherNumber",
                "FunderName",
                "FunderNumber",
                "EmergencyName",
                "EmergencyNumber",
                "EmergencyRelation"), show="headings", yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.tree.place(x=0,y=0, width=843, height=595)
        y_scroll.config(command=self.tree.yview)
        x_scroll.config(command=self.tree.xview)
        y_scroll.place(x=860,y=17.5,width=22,height=613.5)
        x_scroll.place(x=18, y=610, width=843, height=22)

        self.tree.heading("FirstName", text="First Name", anchor=W)
        self.tree.heading("Surname", text="Surname", anchor=W)
        self.tree.heading("MiddleName", text="Middle Name", anchor=W)
        self.tree.heading("BirthDate", text="Birth Date", anchor=W)
        self.tree.heading("StudentID", text="Student ID", anchor=CENTER)
        self.tree.heading("Class", text="Class", anchor=CENTER)
        self.tree.heading("StudentNumber", text="Student's Number", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Email", text="Email", anchor=W)
        self.tree.heading("FatherName", text="Father's Name", anchor=W)
        self.tree.heading("MotherName", text="Mother's Name", anchor=W)
        self.tree.heading("FatherJob", text="Father's Job", anchor=W)
        self.tree.heading("MotherJob", text="Mother's Job", anchor=W)
        self.tree.heading("FatherNumber", text="Father's Number", anchor=W)
        self.tree.heading("MotherNumber", text="Mother's Number", anchor=W)
        self.tree.heading("FunderName", text="Funder's Name", anchor=W)
        self.tree.heading("FunderNumber", text="Funder's Number", anchor=W)
        self.tree.heading("EmergencyName", text="Emergency's Name", anchor=W)
        self.tree.heading("EmergencyNumber", text="Emergency's Number", anchor=W)
        self.tree.heading("EmergencyRelation", text="Emergency's Relation", anchor=W)

        self.tree.column("FirstName", width=100)
        self.tree.column("Surname", width=100)
        self.tree.column("MiddleName", width=100)
        self.tree.column("BirthDate", width=100)
        self.tree.column("StudentID", width=100, anchor=CENTER)
        self.tree.column("Class", width=100, anchor=CENTER)
        self.tree.column("StudentNumber", width=150)
        self.tree.column("Gender", width=100)
        self.tree.column("Address", width=150)
        self.tree.column("Email", width=170)
        self.tree.column("FatherName", width=150)
        self.tree.column("MotherName", width=150)
        self.tree.column("FatherJob", width=150)
        self.tree.column("MotherJob", width=150)
        self.tree.column("FatherNumber", width=150)
        self.tree.column("MotherNumber", width=150)
        self.tree.column("FunderName", width=150)
        self.tree.column("FunderNumber", width=150)
        self.tree.column("EmergencyName", width=150)
        self.tree.column("EmergencyNumber", width=150)
        self.tree.column("EmergencyRelation", width=150)
        self.fetch_data()
        self.tree.bind("<ButtonRelease-1>", self.get_cursor)


        ##################################################################
        ###################### Buttons ##############################
        ##################################################################


        update_button = ttk.Button(info_frame, width=10, padding=2, text='Update', command=self.update_values)
        update_button.place(x=10, y=570)

        clear_button = ttk.Button(info_frame, width=10, padding=2, text='Clear', command=self.clear_values)
        clear_button.place(x=10, y=620)

        delete_button = ttk.Button(info_frame, width=10, padding=2, text='Delete', command=self.delete_values)
        delete_button.place(x=130, y=570)

        back_button = ttk.Button(info_frame, width=10, padding=2, text='Back', command=self.back_go)
        back_button.place(x=130, y=620)

        add_button = ttk.Button(info_frame, width=10, padding=2, text='Add', command=self.add_new_student)
        add_button.place(x=260, y=570)

        exit_button = ttk.Button(info_frame, width=10, padding=2, text='Exit App', command=self.exit_com)
        exit_button.place(x=260, y=620)

    def pick_date(self, event):
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme('arc')
        self.date_win.grab_set()
        self.date_win.title('Choose Date of birth')
        self.date_win.geometry('250x220+590+370')
        self.date_win.attributes('-topmost', True)
        self.cal = Calendar(self.date_win, selectmode='day', date_pattern='mm/dd/y')
        self.cal.place(x=0, y=0)

        okay_btn = ttk.Button(self.date_win, text='Okay', command=self.grab)
        okay_btn.place(x=80, y=180)

    def grab(self):
        self.birth_entry.delete(0, END)
        self.birth_entry.configure(fg='black')
        self.birth_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def clear_values(self):
        self.FirstName.set('')
        self.Surname.set('')
        self.MiddleName.set('')
        self.BirthDate.set('')
        self.StudentID.set('')
        self.YearLevel.set('')
        self.StudentNum.set('')
        self.Gender.set('')
        self.Address.set('')
        self.Email.set('')
        self.FatherName.set('')
        self.MotherName.set('')
        self.FatherOcc.set('')
        self.MotherOcc.set('')
        self.FatherNum.set('')
        self.MotherNum.set('')
        self.FunderName.set('')
        self.FunderNum.set('')
        self.EmeName.set('')
        self.EmeNum.set('')
        self.EmeRelation.set('')

    def add_new_student(self):
        if self.FirstName.get() == "" or self.Surname.get() == "" or self.BirthDate.get() == "" or self.StudentID.get() == ""\
                or self.YearLevel.get() == "" or self.StudentNum.get() == "" or self.Gender.get() == "" or self.Address.get() == ""\
                or self.Email.get() == "" or self.FatherName.get() == "" or self.MotherName.get() == "" or self.FatherOcc.get() == ""\
                or self.MotherOcc.get() == "" or self.FatherNum.get() == "" or self.MotherNum.get() == "" or self.FunderName.get() == ""\
                or self.FunderNum.get() == "" or self.EmeName.get() == "" or self.EmeNum.get() == "" or self.EmeRelation.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = sqlite3.connect('Student_Record.db')
            c = conn.cursor()
            c.execute("INSERT INTO Student_Data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (self.FirstName.get(), self.Surname.get(), self.MiddleName.get(), self.BirthDate.get(),
                       self.StudentID.get(), self.YearLevel.get(), self.StudentNum.get(), self.Gender.get(), self.Address.get(), self.Email.get(),
                       self.FatherName.get(), self.MotherName.get(), self.FatherOcc.get(), self.MotherOcc.get(), self.FatherNum.get(), self.MotherNum.get(),
                       self.FunderName.get(), self.FunderNum.get(), self.EmeName.get(), self.EmeNum.get(), self.EmeRelation.get()))
            conn.commit()
            self.fetch_data()
            self.clear_values()
            conn.close()
            messagebox.showinfo('Success', 'New Student Record has been Added')

    def fetch_data(self):
        conn = sqlite3.connect('Student_Record.db')
        c = conn.cursor()
        c.execute("SELECT * from Student_Data")
        rows = c.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('',END,values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, ev):
        info = self.tree.focus()
        content = self.tree.item(info)
        row = content['values']
        self.FirstName.set(row[0])
        self.Surname.set(row[1])
        self.MiddleName.set(row[2])
        self.BirthDate.set(row[3])
        self.StudentID.set(row[4])
        self.YearLevel.set(row[5])
        self.StudentNum.set(row[6])
        self.Gender.set(row[7])
        self.Address.set(row[8])
        self.Email.set(row[9])
        self.FatherName.set(row[10])
        self.MotherName.set(row[11])
        self.FatherOcc.set(row[12])
        self.MotherOcc.set(row[13])
        self.FatherNum.set(row[14])
        self.MotherNum.set(row[15])
        self.FunderName.set(row[16])
        self.FunderNum.set(row[17])
        self.EmeName.set(row[18])
        self.EmeNum.set(row[19])
        self.EmeRelation.set(row[20])

    def update_values(self):
        conn = sqlite3.connect('Student_Record.db')
        c = conn.cursor()
        c.execute("UPDATE Student_Data set FirstName=?, Surname=?,MiddleName=?,BirthDate=?, "
                  "Class=?,StudentNumber=?,Gender=?,Address=?,Email=?,FatherName=?,MotherName=?,"
                  "FatherJob=?,MotherJob=?,FatherNumber=?,MotherNumber=?,FunderName=?,FunderNumber=?,EmergencyName=?,"
                  "EmergencyNumber=?,EmergencyRelation=? where StudentID=?",
                  (self.FirstName.get(), self.Surname.get(), self.MiddleName.get(), self.BirthDate.get(),
                   self.YearLevel.get(), self.StudentNum.get(), self.Gender.get(),
                   self.Address.get(), self.Email.get(),
                   self.FatherName.get(), self.MotherName.get(), self.FatherOcc.get(), self.MotherOcc.get(),
                   self.FatherNum.get(), self.MotherNum.get(),
                   self.FunderName.get(), self.FunderNum.get(), self.EmeName.get(), self.EmeNum.get(),
                   self.EmeRelation.get(), self.StudentID.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        self.clear_values()
        messagebox.showinfo('Success', 'Student Record has been Updated.')

    def delete_values(self):
        try:
            tree_view_content = self.tree.focus()
            tree_view_items = self.tree.item(tree_view_content)
            tree_view_values = tree_view_items['values'][1]
            ask = messagebox.askyesno("Warning", "Are you sure you want to delete the record?")
            if ask is True:
                conn = sqlite3.connect('Student_Record.db')
                c = conn.cursor()
                c.execute("DELETE FROM Student_Data where StudentID=?", [self.StudentID.get()])
                conn.commit()
                self.fetch_data()
                conn.close()
                self.clear_values()
                messagebox.showinfo("Success", "Record has been Deleted.")
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error", "There has been an error in deleting the record. Please make sure you have clicked on a record.")

    def back_go(self):
        self.root.destroy()
        import HomePage

    def exit_com(self):
        quit = messagebox.askyesno("Exit", "Do you want to exit?", parent=root)
        if quit == True:
            self.root.quit()


root = Tk()
ob = Manage_std(root)
root.mainloop()

