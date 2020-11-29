from clip import App
from clip import MyTableWidget 
ls = []         
last_oprnd = []
history = []


def calculations(oprnd1, oprnd2, op):  
    global ans
    if op == '+':
        ans = float(oprnd1)+float(oprnd2)    
    elif op == '-':
        ans = float(oprnd1) - float(oprnd2)
    elif op == '*':
        ans = float(oprnd1) * float(oprnd2)
    elif op == '/':
        ans = float(oprnd1) / float(oprnd2)
    elif op == '^':
        ans = float(oprnd1) ** float(oprnd2)
    elif op == '%':
        ans = float(oprnd1) % float(oprnd2)
    else:
        pass
    history.append(str(oprnd1)+str(op)+str(oprnd2))
    last_oprnd.insert(0, ans)

    if ans.is_integer():
        ans = int(ans)
        return ans
    else:
        return ans
        

def reset(self): # function to reset the previous operands and operator
    op = ''
    oprnd1= ''
    oprnd2=''
    self.label.clear()
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
        op = ls[0]
        ind = txt.find(op)
        oprnd1 = txt[:ind]
        oprnd2 = txt[ind+1:]

        try:
            result = calculations(oprnd1, oprnd2, op)
        except ValueError:
            oprnd1 = last_oprnd[0]
            result = calculations(oprnd1, oprnd2, op)
        
        reset(self)
        self.label.setText(str(result))


def show_history(self):
    reset(self)
    self.label.setText(history[-1])
