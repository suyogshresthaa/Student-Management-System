import sqlite3

conn = sqlite3.connect('Student_Record.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS User_Data"
          "(Username TEXT, Password TEXT)")
conn.commit()
conn.close()





