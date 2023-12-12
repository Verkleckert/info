# Commands and synax
#
# tst
# jmp
# dec
# inc
# hlt
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# if (var_1 == var_2) {};
# 

import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Window with Buttons and Table")
        
        # Text field
        self.text_input = tk.Text(root, height=30, width=40)
        self.text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Buttons
        button1 = tk.Button(root, text="Compile", command=self.function1, height=2, width=13)
        button1.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

        button2 = tk.Button(root, text="RUN!!!", command=self.function2, height=2, width=13)
        button2.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

        button3 = tk.Button(root, text="Machine Code WIP", command=self.function3, height=2, width=13)
        button3.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

        # Table
        self.tree = ttk.Treeview(root, columns=("Column 1", "Column 2"), show="headings")
        self.tree.heading("Column 1", text="Column 1")
        self.tree.heading("Column 2", text="Column 2")
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10) 

        # Add some sample data to the table
        self.add_data_to_table("Data 1", "Value 1")
        self.add_data_to_table("Data 2", "Value 2")
        self.add_data_to_table("Data 3", "Value 3")

    def function1(self):
        print("Function 1 executed")

    def function2(self):
        print("Function 2 executed")

    def function3(self):
        print("Function 3 executed")

    def add_data_to_table(self, col1_data, col2_data):
        self.tree.insert("", tk.END, values=(col1_data, col2_data))
        
    def refreshRomList(self, data):
        for entry in data:
            self.tree.insert

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()







class parser:
  def __init__(self) -> None:
    pass
  
  def parseRomIndexes():
    pass
  
  def maxIndex():
    pass