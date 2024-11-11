import sys 
from PyQt5.QtWidgets import *

class Tetris(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T E T R I S")
        self.setGeometry(300,200,300,400)
        self.btn=QPushButton("1",self)
        self.btn.setGeometry(50,50,50,50)
        self.btn_2=QPushButton("2", self)
        self.btn_2.setGeometry(100,50,50,50)
        self.btn_3=QPushButton("3", self)
        self.btn_3.setGeometry(150,50,50,50)
        self.btn_4=QPushButton("4", self)
        self.btn_4.setGeometry(200,50,50,50)

    

        self.btn.clicked.connect(self.g_harfi)
        self.btn_2.clicked.connect(self.kvadrat)
        self.btn_3.clicked.connect(self.chiziq)
        self.btn_4.clicked.connect(self.zig_zag)

        
    def g_harfi (self):
        self.wid=G_harf()
        self.wid.show()
    def kvadrat (self):
        self.wid=Kvadrat()
        self.wid.show()
    def chiziq(self):
        self.wid=Chiziq()
        self.wid.show()
    def zig_zag(self):
        self.wid=Zig_zag()
        self.wid.show()

class G_harf(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T E T R I S")
        self.setGeometry(300,200,300,400)
        self.but=QPushButton("", self)
        self.but.setGeometry(100,100,50,50)
        self.but.setStyleSheet("background-color: blue; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_2=QPushButton("",self)
        self.but_2.setGeometry(151,100,50,50)
        self.but_2.setStyleSheet("background-color: blue; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_3=QPushButton("",self)
        self.but_3.setGeometry(100,151,50,50)
        self.but_3.setStyleSheet("background-color: blue;")
        self.but_3.setStyleSheet("background-color: blue; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        
        self.but_4=QPushButton("",self)
        self.but_4.setGeometry(100,202,50,50)
        self.but_4.setStyleSheet("background-color: blue;")
        self.but_4.setStyleSheet("background-color: blue; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        
class Kvadrat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T E T R I S")
        self.setGeometry(300,200,300,400)
        self.but=QPushButton("", self)
        self.but.setGeometry(100,100,50,50)
        self.but.setStyleSheet("background-color: red; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_2=QPushButton("",self)
        self.but_2.setGeometry(151,100,50,50)
        self.but_2.setStyleSheet("background-color: red; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_3=QPushButton("",self)
        self.but_3.setGeometry(100,151,50,50)
        self.but_3.setStyleSheet("background-color: red; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        
        self.but_4=QPushButton("",self)
        self.but_4.setGeometry(151,152,50,50)
        self.but_4.setStyleSheet("background-color: red; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        
class Chiziq(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T E T R I S")
        self.setGeometry(300,200,300,400)
        self.but=QPushButton("", self)
        self.but.setGeometry(100,100,50,50)
        self.but.setStyleSheet("background-color: #8A2BE2; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_2=QPushButton("",self)
        self.but_2.setGeometry(151,100,50,50)
        self.but_2.setStyleSheet("background-color: #8A2BE2; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_3=QPushButton("",self)
        self.but_3.setGeometry(202,100,50,50)
        self.but_3.setStyleSheet("background-color: #8A2BE2; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_4=QPushButton("",self)
        self.but_4.setGeometry(49,100,50,50)
        self.but_4.setStyleSheet("background-color: #8A2BE2; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        

class Zig_zag(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T E T R I S")
        self.setGeometry(300,200,300,400)
        self.but=QPushButton("", self)
        self.but.setGeometry(100,100,50,50)
        self.but.setStyleSheet("background-color: #840909; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_2=QPushButton("",self)
        self.but_2.setGeometry(151,100,50,50)
        self.but_2.setStyleSheet("background-color: #840909; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        self.but_3=QPushButton("",self)
        self.but_3.setGeometry(100,151,50,50)
        self.but_3.setStyleSheet("background-color: #840909; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        
        self.but_4=QPushButton("",self)
        self.but_4.setGeometry(151,49,50,50)
        self.but_4.setStyleSheet("background-color: #840909; border: 2px; box-shadow: 3px 3px 5px gray;border-radius: 5px; padding: 5px;")
        


def main():
    app=QApplication(sys.argv)
    widget=Tetris()
    widget.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()