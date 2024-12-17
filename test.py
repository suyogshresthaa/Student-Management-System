import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Get the available themes
available_themes = ttk.Style().theme_names()

# Print the names of the available themes
for theme in available_themes:
    print(theme)

root.mainloop()


def sort_data(self):
    data = []
    for item in self.tree.get_children():
        values = self.tree.item(item)['values']
        data.append((values[0], values[1], item))

    data.sort(key=lambda x: (x[0], x[1]))  # Sort by First Name and Surname

    for index, item in enumerate(data):
        self.tree.move(item[2], '', index)





    def sort_data(self):
        selected_option = self.sort_combo.get()
        if selected_option == "FirstName":
            self.tree.delete(*self.tree.get_children())
            sorted_items = sorted(self.tree.get_children(), key=lambda x: self.tree.item(x)['values'][0])
            for item in sorted_items:
                values = self.tree.item(item)['values']
                self.tree.insert('', 'end', values=values)
        elif selected_option == "StudentID":
            self.tree.delete(*self.tree.get_children())
            sorted_items = sorted(self.tree.get_children(), key=lambda x: int(self.tree.item(x)['values'][4]))
            for item in sorted_items:
                values = self.tree.item(item)['values']
                self.tree.insert('', 'end', values=values)
        elif selected_option == "Class":
            self.tree.delete(*self.tree.get_children())
            sorted_items = sorted(self.tree.get_children(), key=lambda x: int(self.tree.item(x)['values'][5]))
            for item in sorted_items:
                values = self.tree.item(item)['values']
                self.tree.insert('', 'end', values=values)