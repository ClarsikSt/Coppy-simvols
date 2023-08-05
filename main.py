from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pyperclip

app = QApplication([])
main_win = QWidget()

class Simvol():
    def __init__(self,text):
        self.text = text
        self.me = QPushButton(self.text)
        self.me.setFont(QFont(None, 45))
    def copy(self):
        pyperclip.copy(self.text)
    def relname(self,new):
        self.text = new
        self.me = QPushButton(self.text)
        self.me.setFont(QFont(None, 45))
sc5 = QHBoxLayout()
nextB = QPushButton('▸')
firstB = QPushButton('◂') 
sc5.addWidget(firstB)
sc5.addWidget(nextB)

main_win.setWindowTitle('Coppy paster')
main_win.show()
main_win.page = 0

pmax = 2 -1
simvols = [['☀','☁','☂','☃','☄','★','☆','☇','☈','☉','☊','☋','☌','☍','☎','☏'],
['☟','☠','☐','☑','☒','☓','☔','☕','☖','☗','☘','☙','☚','☛','☝','☞'],[],[],[],[]]

def reset(page):
    global qls,simvols, pmax, main, sc1, sc2, sc3, sc4
    qls = []
    i = 0
    for i in range(16):
        l = Simvol(simvols[main_win.page][i])
        qls.append(l)

    main = QVBoxLayout()
    sc1 = QHBoxLayout()
    sc2 = QHBoxLayout()
    sc3 = QHBoxLayout()
    sc4 = QHBoxLayout()
    
    i = 0
    for i in range(16):
        l = qls[i]
        if i <= 3:
            sc1.addWidget(l.me)
        elif i > 3 and i <= 7:
            sc2.addWidget(l.me)
        elif i > 7 and i <= 11:
            sc3.addWidget(l.me)
        elif i > 11 and i <= 15:
            sc4.addWidget(l.me)
    main.addLayout(sc1)
    main.addLayout(sc2)
    main.addLayout(sc3)
    main.addLayout(sc4)
    main.addLayout(sc5)

    main_win.setLayout(main)
def update():
    i = 0
    for i in range(16):
        l = qls[1]
        l.relname(simvols[main_win.page][i])

    main = QVBoxLayout()
    sc1 = QHBoxLayout()
    sc2 = QHBoxLayout()
    sc3 = QHBoxLayout()
    sc4 = QHBoxLayout()
    
    i = 0
    for i in range(16):
        l = qls[i]
        if i <= 3:
            sc1.addWidget(l.me)
        elif i > 3 and i <= 7:
            sc2.addWidget(l.me)
        elif i > 7 and i <= 11:
            sc3.addWidget(l.me)
        elif i > 11 and i <= 15:
            sc4.addWidget(l.me)
    main.addLayout(sc1)
    main.addLayout(sc2)
    main.addLayout(sc3)
    main.addLayout(sc4)
    main.addLayout(sc5)        

    main_win.setLayout(main)
reset(0)
def nets():
    if main_win.page < pmax:
        main_win.page += 1
        print(1)
        update()
def anrinets():
    if main_win.page > 0:
        main_win.page -= 1
        update()

for w in qls:
    w.me.clicked.connect(w.copy)

main_win.setLayout(main)
nextB.clicked.connect(nets)
firstB.clicked.connect(anrinets)
app.exec_()

