import sqlite3

conn = sqlite3.connect('Student_Record.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Student_Data"
          "(FirstName TEXT, Surname TEXT, MiddleName TEXT, BirthDate TEXT,"
          "StudentID INTEGER, Class TEXT, StudentNumber INTEGER, Gender TEXT, Address TEXT, Email TEXT,"
          "FatherName TEXT, MotherName TEXT, FatherJob TEXT, MotherJob TEXT, FatherNumber INTEGER, MotherNumber INTEGER,"
          "FunderName TEXT, FunderNumber INTEGER, EmergencyName TEXT, EmergencyNumber INTEGER, EmergencyRelation TEXT)")
conn.commit()
conn.close()


