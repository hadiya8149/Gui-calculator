import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication,QGroupBox, QLabel, QGridLayout, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    inp_state = False
    cal = 0
    def __init__(self):
        super().__init__()
        self.title = 'Calculator'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
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
        self.tabs.resize(300,200)
        
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Basic")
        self.tabs.addTab(self.tab2,"Advanced")
        
        # Add label to tab
        self.tab1.layout = QVBoxLayout(self)
        self.label = QLabel('')
        self.label.setStyleSheet("QLabel {border: 1px solid grey; background: white;}")
        self.label.setAlignment(Qt.AlignRight)    
        self.tab1.layout.addWidget(self.label)
        self.tab1.layout.addWidget(self.horizontalGroupBox)
        
        self.tab1.setLayout(self.tab1.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        
    def createGridLayout(self):
        from calculate import get_inp, get_op, eval_nums
        def run_get_inp():
            get_inp(self)
        

        def run_get_op():
            get_op(self)

        def run_eval_nums():
            eval_nums(self)


        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        
        nums = ['7','8','9','4','5','6','1','2','3','0']
        # i used a for loop to generate these coordinates 
        pos = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0)]
        for i in range(len(nums)):
            button = QPushButton(str(nums[i]))
            button.setObjectName("button_%d" %int(nums[i]))
            layout.addWidget(button, pos[i][0], pos[i][1] )
            button.clicked.connect(run_get_inp)

        btn_div = QPushButton('/')
        btn_mul = QPushButton('*')
        btn_sub = QPushButton('-')
        btn_dot = QPushButton('.')
        btn_eql = QPushButton('=')
        btn_add = QPushButton('+')
        btn_div.clicked.connect(run_get_op)
        btn_add.clicked.connect(run_get_op)
        btn_sub.clicked.connect(run_get_op)
        btn_mul.clicked.connect(run_get_op)
        btn_dot.clicked.connect(run_get_inp)
        btn_eql.clicked.connect(run_eval_nums)
        layout.addWidget(btn_div, 1, 3)
        layout.addWidget(btn_mul, 2, 3)
        layout.addWidget(btn_sub, 3, 3)
        layout.addWidget(btn_dot, 4, 1)
        layout.addWidget(btn_add, 4, 2)
        layout.addWidget(btn_eql, 4, 3)
        self.horizontalGroupBox.setLayout(layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
