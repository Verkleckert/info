# Commands and synax
#
# tst
# jmp
# dec
# inc
# hlt
#
#
# TOOLS
# https://bonsai.dibaku.de/
# https://www.inf-schule.de/rechner/bonsai/cpu/operationswerk/i_r
#
#
#
# Notes
# inc ≙ 1
# dec ≙ 2
# jmp ≙ 3
# tst ≙ 4
# hlt ≙ 5
#
#
# ANALYSIS
#
# jmp 1
# jmp 2
# jmp 3
# inc 1
# inc 2
# inc 3
# dec 0
# dec 1
# dec 2
#
# gives following code
#
# 10000001
# 10000010
# 10000011
# 00010011
# 00011101
# 00100111
# 01001001
# 01010011
# 01011101
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


from visual_automata.fa.dfa import VisualDFA
import matplotlib.pyplot as plt
from automata.fa.dfa import DFA
from ply import lex, yacc
from tkinter import ttk
import tkinter as tk
import numpy as np
import sys
import os

import classes as cmds

class UIWindow:
  def __init__(self, root, parser):
    self.root = root
    self.parser = parser
    self.root.title("Tkinter Window with Buttons and Table")
    self.data = [
      0b10100101,
      0b10101111,
      0b10100110,
      0b10101001,
    ]
    self.compiled = [
      "TST 1",
      "JMP 3",
      "HLT  ",
      "INC 0",
      "DEC 1",
      "JMP 0",
      "#    3",
      "#    2",
      ";Register 1 : 1.Summand",
      ";Register 2 : 2.Summand",
      ";Ergebnis der Rechnung in Register 1",
    ]

    # Buttons
    button1 = tk.Button(root, text="Compile", command=self.compileButton, height=2, width=13)
    button1.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

    button2 = tk.Button(root, text="RUN!!!", command=self.runButton, height=2, width=13)
    button2.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

    button3 = tk.Button(root, text="Machine Code WIP", command=self.MachineCodeButton, height=2, width=13)
    button3.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

    # Table
    self.tree = ttk.Treeview(root, columns=("address", "data"), show="headings")
    self.tree.heading("address", text="Address")
    self.tree.heading("data", text="Data")
    self.tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10) 
    
    # Text field
    self.text_input = tk.Text(root, height=30, width=40)
    self.text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    self.refreshRomList()

  def compileButton(self):
    self.parser.parseCode(self.text_input.get("1.0", tk.END))
    f = open("C:\\Users\\tim53\Desktop\\bonsai22\\COMPILED.BON", "w")
    for line in self.compiled:
      f.write(line + "\n")
    f.close()

  def runButton(self):
    os.system('"C:\\Program Files (x86)\\DOSBox-0.74-3\\DOSBox.exe"')

  def MachineCodeButton(self):
    print("Function 3 executed")

  def add_data_to_table(self, col1_data, col2_data):
    self.tree.insert("", tk.END, values=(col1_data, col2_data))
  
  def refreshRomList(self):
    self.clearTree()
    for index in range(0, len(self.data)):
      self.tree.insert("", tk.END, values=(index, self.data[index]))
      
  def clearTree(self):
    for item in self.tree.get_children():
      self.tree.delete(item)
  
  def getLastProgrammAddress(self) -> int:
    return int(len(self.compiled) -1)


class Parser:
  compiled = []
  tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'IF',
    'LPAREN',
    'RPAREN',
    'LSPAREN',
    'RSPAREN',
    'EQUALS',
    'INDEX',
    'SEMICOLON',
  )
  t_PLUS = r'\+'
  t_MINUS = r'-'
  t_TIMES = r'\*'
  t_DIVIDE = r'/'
  t_IF = r'[IF]'
  t_LPAREN = r'\('
  t_RPAREN = r'\)'
  t_LSPAREN = r'\{'
  t_RSPAREN = r'\}'
  t_EQUALS = r'='
  t_SEMICOLON = r';'
  
  def t_INDEX(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t
  
  def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
  
  t_ignore = ' \t\n'
  
  def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
  
  lexer = lex.lex()
    
  def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | term
    '''
      
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

  def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
         | factor
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

  def p_factor(p):
    '''
    factor : NUMBER
           | LPAREN expression RPAREN
    '''
    if len(p) == 4:
      p[0] = p[2]
      # p[0] = "Factor (_)"
    else:
      p[0] = p[1]
      # p[0] = "Factor _"
  
  def p_assignment(p):
    '''
    assignment : INDEX EQUALS expression SEMICOLON
    '''
    # p[0] = p[3] 
    p[0] = "SET VAR"

  def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression EQUALS EQUALS NUMBER RPAREN LSPAREN expression RSPAREN
    '''
    # if p[3] == p[5]:
    #   p[0] = p[7]
    p[0] = "IF"

  # Error rule for syntax errors
  def p_error(p):
    print("Syntax error")
    
  parserYacc = yacc.yacc()

  def __init__(self) -> None:
    pass
  
  def parseCode(self, inputCode):
    print(inputCode)
    result = self.parserYacc.parse(inputCode)
    print(f"Result: {result}")
  
  def parseRomIndexes():
    pass
  
  def maxIndex():
    pass

if __name__ == "__main__":
  root = tk.Tk()
  parser = Parser()
  app = UIWindow(root, parser)
  root.mainloop()
