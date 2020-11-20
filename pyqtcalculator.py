import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout,
                             QGroupBox, QLabel, QPushButton, QVBoxLayout,
                             )
ls = []
history = []
 # inp state is true when the text label is empty if it is not empty 

class App(QDialog):
    # calculator state
    inp_state = False
    cal = 0
    def __init__(self):
        super().__init__()
        #string value
        self.setWindowTitle('Calculator')
        self.setGeometry(0,0,500,500)
        self.setStyleSheet('background-color: white;')                       
        self.createGridLayout()

#main wrapper for grid layout
        self.label = QLabel('')
        self.label.setStyleSheet("QLabel {border: 1px solid black; background: white;}")
        self.label.setAlignment(Qt.AlignRight)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.label)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout) 

    def calculations(oprnd1, oprnd2, op):
        global ans
        if op == '+':
            ans = float(oprnd1)+float(oprnd2)    
            App.reset()
        elif op == '-':
            ans = float(oprnd1) - float(oprnd2)
            App.reset()
        elif op == '*':
            ans = float(oprnd1) * float(oprnd2)
            App.reset()
        elif op == '/':
            ans = float(oprnd1) / float(oprnd2)
            App.reset()
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
        
        self.get_inp()   
        

    
    def eval_nums(self):
            txt = self.label.text()
            self.label.clear()
            op = ls[0]
            ind = txt.find(op)
            oprnd1 = txt[:ind]
            oprnd2 = txt[ind+1:]
            try:
                result = App.calculations(oprnd1, oprnd2, op)
                
            except ValueError:
                oprnd1 = history[-1]
                result = App.calculations(oprnd1, oprnd2, op)
            self.label.setText(str(result))
             

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        ls = ['7','8','9','4','5','6','1','2','3','0']
        
        pos = []
        for i in range(1,5):
            for k in range(0,3):
                pos.append((i,k))
                if i == 4:
                    break
        for i in range(len(ls)):
            button = QPushButton(str(ls[i]))
            button.setObjectName("button_%d" %int(ls[i]))
            layout.addWidget(button, pos[i][0], pos[i][1] )
            button.clicked.connect(self.get_inp)
        
        btn_div = QPushButton('/')
        btn_div.setObjectName('buttondiv')
        btn_mul = QPushButton('*')
        btn_sub = QPushButton('-')
        btn_dot = QPushButton('.')
        btn_eql = QPushButton('=')
        btn_add = QPushButton('+')
        
        layout.addWidget(btn_div, 1, 3)
        layout.addWidget(btn_mul, 2, 3)
        layout.addWidget(btn_sub, 3, 3)
        layout.addWidget(btn_dot, 4, 1)
        layout.addWidget(btn_eql, 4, 2)
        layout.addWidget(btn_add, 4, 3)
        
        btn_div.clicked.connect(self.get_op)
        btn_add.clicked.connect(self.get_op)
        btn_sub.clicked.connect(self.get_op)
        btn_mul.clicked.connect(self.get_op)
        btn_dot.clicked.connect(self.get_inp)
        btn_eql.clicked.connect(self.eval_nums)
        self.horizontalGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
