from re import S
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
from VideoPageLogic import *


class NewWindow(QWidget):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setGeometry(600,400,400,300)
        self.setStyleSheet("background-color : black;")
        

    def addPlayList(self):
        self.explainLabel = QLabel(self)
        self.explainLabel.setGeometry(70,80,320,16)
        self.explainLabel.setStyleSheet("color : white;\n"
            "font-size : 16pt;")
        self.explainLabel.setText("Input PlayList's Name what you want")

        self.inputLineEdit = QLineEdit(self)
        self.inputLineEdit.setGeometry(20,110,360,30)
        self.inputLineEdit.setStyleSheet("background-color : rgb(20,20,20);\n"
            "color : white;\n"
            "padding-left: 5px;\n"
            "border-radius: 1px;\n")

        self.warnLabel = QLabel(self)
        self.warnLabel.setGeometry(330,145,60,16)
        self.warnLabel.setStyleSheet("color : red;\n"
            "font-size : 16pt;")
        
        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setGeometry(95,170,100,50)
        self.cancelBtn.setStyleSheet("background-color : rgb(60,60,60);\n"
            "border-radius: 10px;\n"
            "color : white;\n"
            "font-size : 20pt;")
        self.cancelBtn.setText("Cancel")

        self.enrollBtn = QPushButton(self)  
        self.enrollBtn.setGeometry(205,170,100,50)
        self.enrollBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
            "border-radius: 10px;\n"
            "color : white;\n"
            "font-size : 20pt;")
        self.enrollBtn.setText("Enroll")


    def addVideo(self):
        self.addPlayList()
        self.explainLabel.setText("Input YouTube's URL what you want")
        

    def delConfirm(self):
        self.explainLabel = QLabel(self)
        self.explainLabel.setGeometry(100,100,320,16)
        self.explainLabel.setStyleSheet("color : white;\n"
            "font-size : 16pt;")
        self.explainLabel.setText("You really want to Delete?")

        self.noBtn = QPushButton(self)
        self.noBtn.setGeometry(95,150,100,50)
        self.noBtn.setStyleSheet("background-color : rgb(60,60,60);\n"
            "border-radius: 10px;\n"
            "color : white;\n"
            "font-size : 20pt;")
        self.noBtn.setText("No")

        self.yesBtn = QPushButton(self)  
        self.yesBtn.setGeometry(205,150,100,50)
        self.yesBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
            "border-radius: 10px;\n"
            "color : white;\n"
            "font-size : 20pt;")
        self.yesBtn.setText("Yes")

    

