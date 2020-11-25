import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout,
                             QGroupBox, QLabel, QPushButton, QVBoxLayout,
                             )
from clip import App
from clip import MyTableWidget 
ls = []         
history = []

def calculations(oprnd1, oprnd2, op):
    
    global ans
    if op == '+':
        ans = float(oprnd1)+float(oprnd2)    
        reset()
    elif op == '-':
        ans = float(oprnd1) - float(oprnd2)
        reset()
    elif op == '*':
        ans = float(oprnd1) * float(oprnd2)
        reset()
    elif op == '/':
        ans = float(oprnd1) / float(oprnd2)
        reset()
    else:
        print("enter valid operator")
    if ans.is_integer():
        ans = int(ans)
        history.insert(0, ans)
        return ans
    else:
        return ans

def reset(): # function to reset the previous operands and operator
    op = ''
    oprnd1= ''
    oprnd2=''
    App.inp_state = True
def get_inp(self):
    button = self.sender()
    if App.inp_state == True:
        self.label.clear()
        txt = format(self.label.text()+str(button.text()))
        self.label.setText(txt)
        App.inp_state = False
    else:
        txt = format(self.label.text()+str(button.text()))
        self.label.setText(txt)


def get_op(self):              
    button = self.sender()
    op = button.text() 
    ls.insert(0, op)   
    get_inp(self)   
    

def eval_nums(self):
        txt = self.label.text()
        self.label.clear()
        op = ls[0]
        ind = txt.find(op)
        oprnd1 = txt[:ind]
        oprnd2 = txt[ind+1:]
        print('this is ind', ind)
        print('this is oprnd1', oprnd1)
        print('this is oprnd2', oprnd2)
        try:
            result = calculations(oprnd1, oprnd2, op)
            
        except ValueError:
            oprnd1 = history[0]
            print(oprnd1)
            result = calculations(oprnd1, oprnd2, op)
        self.label.setText(str(result))