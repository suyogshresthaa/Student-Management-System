from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

#window creation
class View_Std:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")
        self.root.geometry('1366x768')
        self.root.configure(bg='black')

        title = Label(self.root,text='View Student Records ',font=('Comic Sans MS',35),border=5,relief=RIDGE,fg='black',bg='#57a1f8')
        title.pack(fill=X)

        #-------------------Variables-------------------------
        self.search_by = StringVar()
        self.search_text = StringVar()

        ##################################################################
        ###################### Record Frame##############################
        ##################################################################

        rcd_frame = Frame(self.root, width=1345, height=630, bg='#57a1f8', border=5, relief=RIDGE)
        rcd_frame.place(x=10, y=70)

        # ------------------------- Tree Frame ---------------------------
        tree_frame = Frame(rcd_frame, width=1310, height=600, bg='black', border=7, relief=RIDGE)
        tree_frame.place(x=10, y=10)

        # ------------------------- Search ---------------------------
        search_label = Label(rcd_frame, text='Search By: ', bg='black', fg='#57a1f8', font=('Comic Sans MS', 22))
        search_label.place(x=20, y=30)

        search_combo = ttk.Combobox(rcd_frame, font=('Comic Sans MS', 14, 'bold'), state='readonly',
                                   width=15, textvariable=self.search_by)

        search_combo['values'] = ['FirstName', 'StudentID', 'Class']
        search_combo.place(x=145, y=37)

        search_entry = Entry(rcd_frame, border=2, relief=FLAT, bg='#57a1f8', fg='black',
                          font=('Comic Sans MS', 15), textvariable=self.search_text)
        search_entry.place(x=330, y=34, width=200)

        # ------------------------- Sort ---------------------------
        self.sort_label = Label(rcd_frame, text='Sort By: ', bg='black', fg='#57a1f8', font=('Comic Sans MS', 22))
        self.sort_label.place(x=900, y=30)

        self.sort_combo = ttk.Combobox(rcd_frame, font=('Comic Sans MS', 14, 'bold'), state='readonly',
                                    width=15)

        self.sort_combo['values'] = ['FirstName', 'StudentID', 'Class']
        self.sort_combo.place(x=1000, y=38)

        # ------------------------- Tree View ---------------------------
        s = ttk.Style(root)
        s.theme_use("clam")
        s.configure("Treeview.Heading", font=('Comic Sans MS', 14, "bold"), foreground="black",
                    background="#57a1f8")
        s.configure("TButton", background="#57a1f8", border=20, relief=RIDGE, font=("Comic Sans MS", 14, "bold"))

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

        self.tree.place(x=0, y=65, width=1295, height=500)
        y_scroll.config(command=self.tree.yview)
        x_scroll.config(command=self.tree.xview)
        y_scroll.place(x=1290, y=86, width=22, height=516)
        x_scroll.place(x=18, y=580, width=1272, height=22)

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
        self.tree.column("EmergencyNumber", width=155)
        self.tree.column("EmergencyRelation", width=155)
        self.fetch_data()


        ##################################################################
        ###################### Buttons ##############################
        ##################################################################



        manage_button = ttk.Button(self.root, width=30, padding=2, text='Manage Existing Student Records', command=self.manage_page)
        manage_button.place(x=370, y=710)

        exit_button = ttk.Button(self.root, width=30, padding=2, text='Exit Application', command=self.exit_page)
        exit_button.place(x=1055, y=710)

        back_button = ttk.Button(self.root, width=30, padding=2, text='Back', command=self.back_page)
        back_button.place(x=720, y=710)

        add_button = ttk.Button(self.root, width=30, padding=2, text='Add New Student Records', command=self.add_page)
        add_button.place(x=30, y=710)

        search_button = ttk.Button(tree_frame, width=10, padding=2, text='Search', command=self.search_data)
        search_button.place(x=550, y=20)

        show_button = ttk.Button(tree_frame, width=10, padding=2, text='Show All', command=self.fetch_data)
        show_button.place(x=680, y=20)

        sort_button = ttk.Button(tree_frame, width=10, padding=2, text='Sort', command=self.sort_data)
        sort_button.place(x=1170, y=20)

    ##########################################################################
    ##########################################################################
    ##########################################################################

    def manage_page(self):
        self.root.destroy()
        import Manage_std

    def exit_page(self):
        quit = messagebox.askyesno("Exit", "Do you want to exit?", parent=root)
        if quit == True:
            self.root.quit()

    def back_page(self):
        self.root.destroy()
        import HomePage


    def add_page(self):
        self.root.destroy()
        import Add_Std

    def fetch_data(self):
        conn = sqlite3.connect('Student_Record.db')
        c = conn.cursor()
        c.execute("SELECT * from Student_Data")
        rows = c.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', END, values=row)
            conn.commit()
        conn.close()

    def search_data(self):
        if self.search_by.get() == "" or self.search_text.get() == "":
            messagebox.showerror('Error', 'Please select a searching option')
        else:
            conn = sqlite3.connect('Student_Record.db')
            c = conn.cursor()
            c.execute("SELECT * FROM Student_Data WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
            rows = c.fetchall()
            if len(rows) != 0:
                self.tree.delete(*self.tree.get_children())
                for row in rows:
                    self.tree.insert('', END, values=row)
                conn.commit()
            else:
                messagebox.showerror("Error", "No matching records found")
            conn.close()

    def sort_data(self):
        sort_by = self.sort_combo.get()
        if sort_by == "":
            messagebox.showerror("Error", "Please select a sorting option")
            return

        # Get the data from the treeview
        data = []
        for item in self.tree.get_children():
            values = self.tree.item(item)['values']
            data.append(values)

        if sort_by == "FirstName":
            data.sort(key=lambda x: x[0])  # Sort by First Name
        elif sort_by == "StudentID":
            data.sort(key=lambda x: int(x[4]))  # Sort by Student ID
        elif sort_by == "Class":
            data.sort(key=lambda x: int(x[5]))  # Sort by Class

        # Clear the treeview
        self.tree.delete(*self.tree.get_children())

        # Insert sorted data into the treeview
        for item in data:
            self.tree.insert('', END, values=item)


root = Tk()
ob = View_Std(root)
root.mainloop()