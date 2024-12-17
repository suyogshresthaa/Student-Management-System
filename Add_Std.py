from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import sqlite3
from tkinter import ttk
from ttkthemes import themed_tk as tk

class Add_Std:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")
        self.root.geometry('1366x768')
        self.root.configure(bg='black')

        title = Label(self.root,text='Student Registration Form',font=('Comic Sans MS',40),border=5,relief=RIDGE,fg='black',bg='#57a1f8')
        title.pack(fill=X)

        titleb = Label(self.root, text='*** ALL VALUES ARE REQUIRED TO BE FILLED ***', font=('Arial', 15), border=5, relief=RIDGE,
                      fg='black', bg='#57a1f8')
        titleb.pack(side=BOTTOM, fill=X)

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
        ######################Personal Frame##############################
        ##################################################################

        personal_frame = Frame(self.root, width=800, height=150, bg='#57a1f8',border=5,relief=RIDGE)
        personal_frame.place(x=50, y=100)

        p_title = Label(personal_frame,text="Child's Personal Information",font=('Arial',20,'bold'),fg='black',bg='#57a1f8')
        p_title.place(x=0, y=0)

        # ------------------------- First Name ---------------------------
        fname_label = Label(personal_frame, text='First Name: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        fname_label.place(x=0, y=30)

        fname_entry = Entry(personal_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.FirstName)
        fname_entry.place(x=90, y=30, width=230)

        fname_line = Canvas(personal_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        fname_line.place(x=90, y=50)

        # ------------------------- SurName ---------------------------
        sname_label = Label(personal_frame, text='Surname: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        sname_label.place(x=380, y=30)

        sname_entry = Entry(personal_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.Surname)
        sname_entry.place(x=457, y=30, width=230)

        sname_line = Canvas(personal_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        sname_line.place(x=457, y=50)

        # ------------------------- Middle Name ---------------------------
        mname_label = Label(personal_frame, text='Middle Name (If Any): ', bg='#57a1f8', fg='black', font=('Arial', 16))
        mname_label.place(x=0, y=70)

        mname_entry = Entry(personal_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.MiddleName)
        mname_entry.place(x=162, y=70, width=155)

        mname_line = Canvas(personal_frame, highlightthickness=0, bg='black', width=155, height=1.5)
        mname_line.place(x=162, y=90)

        # ------------------------- Birth ---------------------------
        self.birth_label = Label(personal_frame, text='Birth Date: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        self.birth_label.place(x=380, y=70)

        self.birth_entry = Entry(personal_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                 font=('Arial', 15), textvariable=self.BirthDate)
        self.birth_entry.place(x=465, y=70, width=220)
        self.birth_entry.insert(0, 'dd/mm/yyyy')
        self.birth_entry.bind('<1>', self.pick_date)

        self.birth_line = Canvas(personal_frame, highlightthickness=0, bg='black', width=220, height=1.5)
        self.birth_line.place(x=465, y=90)

        ##################################################################
        ######################Account Frame##############################
        ##################################################################

        account_frame = Frame(self.root, width=800, height=180, bg='#57a1f8',border=5,relief=RIDGE)
        account_frame.place(x=50, y=285)

        a_title = Label(account_frame, text="Child's Other Information", font=('Arial', 20,'bold'), fg='black', bg='#57a1f8')
        a_title.place(x=0, y=0)

        # ------------------------- Student ID ---------------------------
        sID_label = Label(account_frame, text='Student ID: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        sID_label.place(x=0, y=30)

        sID_entry = Entry(account_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                            font=('Arial', 15), textvariable=self.StudentID)
        sID_entry.place(x=90, y=30, width=230)

        sID_line = Canvas(account_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        sID_line.place(x=90, y=50)

        # ------------------------- Class level ---------------------------
        ay_label = Label(account_frame, text='Year Level: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        ay_label.place(x=400, y=30)

        class_combo = ttk.Combobox(account_frame, font=('Arial', 14, 'bold'), state='readonly',
                                         width=20, textvariable=self.YearLevel)

        class_combo['values'] = ['1', '2', '3', '4', '5', '6', '7', '8']
        class_combo.place(x=490, y=32)

        # ------------------------- Student Number ---------------------------
        snumber_label = Label(account_frame, text="Student's Number:", bg='#57a1f8', fg='black', font=('Arial', 16))
        snumber_label.place(x=0, y=70)

        snumber_entry = Entry(account_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                          font=('Arial', 15), textvariable=self.StudentNum)
        snumber_entry.place(x=140, y=70, width=180)

        snumber_line = Canvas(account_frame, highlightthickness=0, bg='black', width=180, height=1.5)
        snumber_line.place(x=140, y=90)

        # ------------------------- Gender ---------------------------
        gen_label = Label(account_frame, text='Gender: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        gen_label.place(x=400, y=70)

        gen_combo = ttk.Combobox(account_frame, font=('Arial', 14, 'bold'), state='readonly',
                                   width=23, textvariable=self.Gender)

        gen_combo['values'] = ['Male', 'Female', 'Other']
        gen_combo.place(x=465, y=72)


        # ------------------------- Full Address ---------------------------
        snumber_label = Label(account_frame, text='Full Address: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        snumber_label.place(x=0, y=110)

        snumber_entry = Entry(account_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.Address)
        snumber_entry.place(x=100, y=110, width=220)

        snumber_line = Canvas(account_frame, highlightthickness=0, bg='black', width=220, height=1.5)
        snumber_line.place(x=100, y=130)

        # ------------------------- Email ---------------------------
        email_label = Label(account_frame, text='Email: ', bg='#57a1f8', fg='black', font=('Arial', 16))
        email_label.place(x=400, y=110)

        email_entry = Entry(account_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                         font=('Arial', 15), textvariable=self.Email)
        email_entry.place(x=455, y=110, width=215)

        email_line = Canvas(account_frame, highlightthickness=0, bg='black', width=215, height=1.5)
        email_line.place(x=455, y=130)

        ##################################################################
        ######################Parent Frame##############################
        ##################################################################

        parent_frame = Frame(self.root, width=800, height=200, bg='#57a1f8',border=5,relief=RIDGE)
        parent_frame.place(x=50, y=500)

        pa_title = Label(parent_frame, text="Child's Parental Information", font=('Arial', 20,'bold'), fg='black', bg='#57a1f8')
        pa_title.place(x=0, y=0)

        # ------------------------- Father ---------------------------
        father_label = Label(parent_frame, text="Father's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        father_label.place(x=0, y=30)

        father_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                          font=('Arial', 15), textvariable=self.FatherName)
        father_entry.place(x=115, y=30, width=230)

        father_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        father_line.place(x=115, y=50)

        # ------------------------- Father Job ---------------------------
        fatherjob_label = Label(parent_frame, text="Father's Occupation: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        fatherjob_label.place(x=0, y=85)

        fatherjob_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.FatherOcc)
        fatherjob_entry.place(x=155, y=85, width=190)

        fatherjob_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=190, height=1.5)
        fatherjob_line.place(x=155, y=105)

        # ------------------------- Mother ---------------------------
        mother_label = Label(parent_frame, text="Mother's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        mother_label.place(x=400, y=30)

        mother_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.MotherName)
        mother_entry.place(x=520, y=30, width=230)

        mother_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        mother_line.place(x=520, y=50)

        # ------------------------- Mother Job ---------------------------
        motherjob_label = Label(parent_frame, text="Mother's Occupation: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        motherjob_label.place(x=400, y=85)

        motherjob_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.MotherOcc)
        motherjob_entry.place(x=560, y=85, width=190)

        motherjob_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=190, height=1.5)
        motherjob_line.place(x=560, y=105)

        # ------------------------- Father Number ---------------------------
        fathernum_label = Label(parent_frame, text="Father's Number: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        fathernum_label.place(x=0, y=140)

        fathernum_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.FatherNum)
        fathernum_entry.place(x=130, y=140, width=215)

        fathernum_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=215, height=1.5)
        fathernum_line.place(x=130, y=160)

        # ------------------------- Mother Number ---------------------------
        motherjob_label = Label(parent_frame, text="Mother's Number: ", bg='#57a1f8', fg='black',
                                font=('Arial', 16))
        motherjob_label.place(x=400, y=140)

        motherjob_entry = Entry(parent_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                                font=('Arial', 15), textvariable=self.MotherNum)
        motherjob_entry.place(x=535, y=140, width=215)

        motherjob_line = Canvas(parent_frame, highlightthickness=0, bg='black', width=215, height=1.5)
        motherjob_line.place(x=535, y=160)

        ##################################################################
        ######################Funder Frame##############################
        ##################################################################

        sponsor_frame = Frame(self.root, width=400, height=150, bg='#57a1f8', border=5, relief=RIDGE)
        sponsor_frame.place(x=900, y=100)

        s_title = Label(sponsor_frame, text='Funding for the Child', font=('Arial', 20,'bold'), fg='black', bg='#57a1f8')
        s_title.place(x=0, y=0)

        # ------------------------- Funder Name ---------------------------
        sponame_label = Label(sponsor_frame, text="Funder's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        sponame_label.place(x=0, y=30)

        sponame_entry = Entry(sponsor_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.FunderName)
        sponame_entry.place(x=120, y=30, width=230)

        sponame_line = Canvas(sponsor_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        sponame_line.place(x=120, y=50)

        # ------------------------- Funder Number ---------------------------
        sponum_label = Label(sponsor_frame, text="Funder's Number: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        sponum_label.place(x=0, y=70)

        sponum_entry = Entry(sponsor_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                              font=('Arial', 15), textvariable=self.FunderNum)
        sponum_entry.place(x=135, y=70, width=217)

        sponum_line = Canvas(sponsor_frame, highlightthickness=0, bg='black', width=217, height=1.5)
        sponum_line.place(x=135, y=90)

        ##################################################################
        ######################Emergency Frame##############################
        ##################################################################

        ecg_frame = Frame(self.root, width=400, height=180, bg='#57a1f8', border=5, relief=RIDGE)
        ecg_frame.place(x=900, y=285)

        ecg_title = Label(ecg_frame, text='Emergency Contact other than Parents', font=('Arial', 20, 'bold'), fg='black',
                        bg='#57a1f8')
        ecg_title.place(x=0, y=0)

        # ------------------------- Emergency Name ---------------------------
        emename_label = Label(ecg_frame, text="Person's Name: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        emename_label.place(x=0, y=30)

        emename_entry = Entry(ecg_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.EmeName)
        emename_entry.place(x=120, y=30, width=230)

        emename_line = Canvas(ecg_frame, highlightthickness=0, bg='black', width=230, height=1.5)
        emename_line.place(x=120, y=50)

        # ------------------------- Emergency Number ---------------------------
        emenum_label = Label(ecg_frame, text="Person's Number: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        emenum_label.place(x=0, y=70)

        emenum_entry = Entry(ecg_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                          font=('Arial', 15), textvariable=self.EmeNum)
        emenum_entry.place(x=135, y=70, width=217)

        emenum_line = Canvas(ecg_frame, highlightthickness=0, bg='black', width=217, height=1.5)
        emenum_line.place(x=135, y=90)

        # ------------------------- Emergency Relation ---------------------------
        emerel_label = Label(ecg_frame, text="Person's Relation to Child: ", bg='#57a1f8', fg='black', font=('Arial', 16))
        emerel_label.place(x=0, y=110)

        emerel_entry = Entry(ecg_frame, highlightthickness=0, relief=FLAT, bg='#57a1f8', fg='black',
                             font=('Arial', 15), textvariable=self.EmeRelation)
        emerel_entry.place(x=195, y=110, width=155)

        emerel_line = Canvas(ecg_frame, highlightthickness=0, bg='black', width=155, height=1.5)
        emerel_line.place(x=195, y=130)

        ##################################################################
        ###################### Buttons ##############################
        ##################################################################

        custom_theme = ttk.Style()
        custom_theme.theme_create('custom_theme', parent='alt',
                                  settings={'TButton': {'configure': {'background': '#57a1f8',
                                                                      'font': ('Arial', 14, 'bold'),
                                                                      'anchor': 'center',
                                                                      'borderwidth': 5,
                                                                      'relief': RIDGE}}})
        custom_theme.theme_use('custom_theme')

        btn_label = Label(self.root, text="Please choose an action after the completion of the form", bg='black', fg='#57a1f8',
                                 font=('Arial', 16))
        btn_label.place(x=896, y=495)

        submit_button = ttk.Button(self.root, width=35, padding=2, text='Submit', command=self.add_student)
        submit_button.place(x=950, y=530)

        clear_button = ttk.Button(self.root, width=35, padding=2, text='Clear', command=self.clear_rec)
        clear_button.place(x=950, y=575)

        back_button = ttk.Button(self.root, width=35, padding=2, text='Back', command=self.go_back)
        back_button.place(x=950, y=620)

        exit_button = ttk.Button(self.root, width=35, padding=2, text='Exit Application', command=self.exit_app)
        exit_button.place(x=950, y=665)


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
            
        okay_btn = ttk.Button(self.date_win, text='Okay', command= self.grab)
        okay_btn.place(x=80, y=180)
            
    def grab(self):
        self.birth_entry.delete(0, END)
        self.birth_entry.configure(fg='black')
        self.birth_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def validate_int(self, P):
        if P == "" or P.isdigit():
            return True
        return False

    def add_student(self):
        student_id = self.StudentID.get()

        if not self.StudentID.get().isdigit():
            messagebox.showerror('Error', 'Student ID must be an integer.')
            return

        if not self.StudentNum.get().isdigit():
            messagebox.showerror('Error', 'Student Number must be an integer.')
            return

        if not self.FatherNum.get().isdigit():
            messagebox.showerror('Error', "Father's Number must be an integer.")
            return

        if not self.MotherNum.get().isdigit():
            messagebox.showerror('Error', "Mother's Number must be an integer.")
            return

        if not self.FunderNum.get().isdigit():
            messagebox.showerror('Error', 'Funder Number must be an integer.')
            return

        if not self.EmeNum.get().isdigit():
            messagebox.showerror('Error', 'Emergency Number must be an integer.')
            return

        if self.FirstName.get() == "" or self.Surname.get() == "" or self.BirthDate.get() == ""\
                or self.YearLevel.get() == "" or self.StudentNum.get() == "" or self.Gender.get() == "" or self.Address.get() == ""\
                or self.Email.get() == "" or self.FatherName.get() == "" or self.MotherName.get() == "" or self.FatherOcc.get() == ""\
                or self.MotherOcc.get() == "" or self.FatherNum.get() == "" or self.MotherNum.get() == "" or self.FunderName.get() == ""\
                or self.FunderNum.get() == "" or self.EmeName.get() == "" or self.EmeNum.get() == "" or self.EmeRelation.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = sqlite3.connect('Student_Record.db')
            c = conn.cursor()

            # Check if the student ID already exists in the database
            c.execute("SELECT * FROM Student_Data WHERE StudentID=?", (student_id,))
            existing_student = c.fetchone()

            if existing_student:
                messagebox.showerror('Error', 'Student ID already exists. Please use a unique Student ID.')
            else:
                c.execute("INSERT INTO Student_Data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                          (self.FirstName.get(), self.Surname.get(), self.MiddleName.get(), self.BirthDate.get(),
                           self.StudentID.get(), self.YearLevel.get(), self.StudentNum.get(), self.Gender.get(), self.Address.get(), self.Email.get(),
                           self.FatherName.get(), self.MotherName.get(), self.FatherOcc.get(), self.MotherOcc.get(), self.FatherNum.get(), self.MotherNum.get(),
                           self.FunderName.get(), self.FunderNum.get(), self.EmeName.get(), self.EmeNum.get(), self.EmeRelation.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'New Student Record has been Added')

    def clear_rec(self):
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

    def go_back(self):
        self.root.destroy()
        import HomePage

    def exit_app(self):
        quit = messagebox.askyesno("Exit", "Do you want to exit?", parent=self.root)
        if quit == True:
            self.root.quit()


root = Tk()
ob = Add_Std(root)
root.mainloop()
