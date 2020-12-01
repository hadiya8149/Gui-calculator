import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication,QGroupBox, QLabel, QGridLayout, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    inp_state = False
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.setWindowTitle(self.title)
        self.setGeometry(0,0 ,200, 300)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
       
        self.layout = QVBoxLayout(self)
        self.createGridLayout()
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        
        

        # Add tabs
        self.tabs.addTab(self.tab1,"Basic")
        self.tabs.addTab(self.tab2,"Advanced")
        # Add label to tab
        self.tab1.layout = QVBoxLayout(self)
        self.label = QLabel('')
        self.label.setStyleSheet("QLabel {border: 1px solid black; background: white;}")
        self.label.setAlignment(Qt.AlignRight)    
        self.tab1.layout.addWidget(self.label)
        self.tab1.layout.addWidget(self.horizontalGroupBox)
        
        self.tab1.setLayout(self.tab1.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    def createGridLayout(self):
        from calculate import get_inp, get_op, eval_nums, reset, show_history
        def run_get_inp():
            get_inp(self)
        
        def run_history():
            show_history(self)
        
        def run_get_op():
            get_op(self)

        def run_eval_nums():
            eval_nums(self)

        def run_reset():
            reset(self) 

        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        
        nums = ['7','8','9','4','5','6','1','2','3','0']
        # i used a for loop to generate these coordinates 
        pos = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0)]
        for i in range(len(nums)):
            button = QPushButton(str(nums[i]))
            layout.addWidget(button, pos[i][0], pos[i][1] )
            button.clicked.connect(run_get_inp)

        btn_div = QPushButton('/')
        btn_mul = QPushButton('*')  
        btn_sub = QPushButton('-')
        btn_dot = QPushButton('.')
        btn_mod = QPushButton('%')
        btn_eql = QPushButton('=')
        btn_add = QPushButton('+')
        btn_pow = QPushButton('^')
        btn_sqrt = QPushButton('√')
        btn_opb = QPushButton('(')
        btn_clb = QPushButton(')')
        btn_re = QPushButton('re')
        btn_clr = QPushButton('C')

        btn_div.clicked.connect(run_get_op)
        btn_add.clicked.connect(run_get_op)
        btn_sub.clicked.connect(run_get_op)
        btn_mul.clicked.connect(run_get_op)
        btn_mod.clicked.connect(run_get_op)
        btn_dot.clicked.connect(run_get_inp)
        btn_eql.clicked.connect(run_eval_nums)
        btn_clr.clicked.connect(run_reset)
        btn_sqrt.clicked.connect(run_get_inp)
        btn_pow.clicked.connect(run_get_op)
        btn_re.clicked.connect(run_history)
        layout.addWidget(btn_div, 1, 3)
        layout.addWidget(btn_mul, 2, 3)
        layout.addWidget(btn_sub, 3, 3)
        layout.addWidget(btn_dot, 4, 1)
        layout.addWidget(btn_mod, 4, 2)
        layout.addWidget(btn_add, 4, 3)
        layout.addWidget(btn_eql, 4,4,1, 2)
        layout.addWidget(btn_re, 1,4)
        layout.addWidget(btn_clr, 1,5)
        layout.addWidget(btn_opb, 2,4)
        layout.addWidget(btn_clb, 2,5)
        layout.addWidget(btn_pow, 3, 4)
        layout.addWidget(btn_sqrt, 3, 5)

        self.horizontalGroupBox.setLayout(layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
