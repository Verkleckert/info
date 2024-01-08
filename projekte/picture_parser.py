import tkinter as tk
from tkinter import ttk

with open('./projekte/in_file.jpg', mode='rb') as file: # b is important -> binary
  fileContent_in = file.read()

with open('./projekte/out_file.jpg', mode='rb') as file: # b is important -> binary
  fileContent_out = file.read()

print(len(fileContent_in))
print(len(fileContent_out))