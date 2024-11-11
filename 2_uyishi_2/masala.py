import sys
from PyQt5.QtWidgets import *
import json

class Registr(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,200,350,200)
        
        self.lay_1=QHBoxLayout()
        self.lab_1=QLabel("Login")
        self.l_ed_1=QLineEdit()
        self.lay_1.addWidget(self.lab_1)
        self.lay_1.addWidget(self.l_ed_1)

        self.lay_2=QHBoxLayout()
        self.lab_2=QLabel("Login")
        self.l_ed_2=QLineEdit()
        self.lay_2.addWidget(self.lab_2)
        self.lay_2.addWidget(self.l_ed_2)

        self.lay_btn=QHBoxLayout()
        self.btn_1=QPushButton("SignIn")
        self.btn_2=QPushButton("SignUp")
        self.lay_btn.addWidget(self.btn_1)
        self.lay_btn.addWidget(self.btn_2)

        self.box=QVBoxLayout()
        self.box.addLayout(self.lay_1)
        self.box.addLayout(self.lay_2)
        self.box.addLayout(self.lay_btn)

        self.setLayout(self.box)

        self.btn_2.clicked.connect(self.registratsiya)
        self.btn_1.clicked.connect(self.kirish)
    
    def kirish(self):
        person=Odam(self.l_ed_1.text(), self.l_ed_2.text())
        dct=person.__dict__
        with open ("malumot.json","r") as file:
            baza=json.load(file)
        baza_lst=baza["baza"]
        lampa=0
        for i in baza_lst:
            if i==dct:
                lampa=1
        if lampa==1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Output")
            msg.setText("Siz tizimga kirdingiz!!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Xatolik")
            msg.setText("Bunday foydalanuvchi mavjud emas!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()


    def registratsiya(self):
        person=Odam(self.l_ed_1.text(), self.l_ed_2.text())
        dct=person.__dict__
        with open ("malumot.json","r") as file:
            baza=json.load(file)
        baza_lst=baza["baza"]
        lampa=0
        for i in baza_lst:
            if i==dct:
                lampa=1
        if lampa==0:
            baza_lst.append(dct)
            baza["baza"]=baza_lst
            with open("malumot.json","w") as file:
                json.dump(baza,file)
            self.l_ed_1.clear()
            self.l_ed_2.clear()
        else:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Xatolik")
            msg.setText("Bunday foydalanuvchi mavjud!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
class Odam:
    def __init__(self, login, parol):
        self.Login=login
        self.Parol=parol


def main():
    app=QApplication(sys.argv)
    window=Registr()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()