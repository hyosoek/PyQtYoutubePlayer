from enum import auto
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *

class SignUpPageLogic:
    def __init__(self,Ui):
        self.ui = Ui
        self.idCheckFlag = False
        self.ui.signUpBtnList[0].clicked.connect(lambda event: self.signUpSeq(event))
        self.ui.signUpBtnList[1].clicked.connect(lambda event: self.idCheck(event))
        self.ui.signUpBtnList[2].clicked.connect(lambda event: self.goToSignIn(event))
        db = DataBase()
        self.userDataTemp = db.dataRead("user","","")

    def idCheck(self,event):
        
        idtemp = self.ui.signUpLineEditList[0].text()
        userIndex = -1
        for i in range(0,len(self.userDataTemp)):
            if self.userDataTemp[i][0] == idtemp:
                userIndex = i #있으면 인덱스 반환

        if userIndex == -1 and idtemp != "": #아이디가 중복존재하지 않고, 빈 입력칸이 아니면
            self.ui.idCheckLabel.setText("Enable!")
            self.ui.idCheckLabel.setStyleSheet("color: green;\n"
            "background-color : rgb(50,50,50);\n"
            "font-size: 13pt;")
            self.ui.signUpLineEditList[0].setDisabled(True)
            self.idCheckFlag = True

        else:
            self.ui.idCheckLabel.setText("Disable!")
            self.ui.idCheckLabel.setStyleSheet("color: red;\n"
            "background-color : rgb(50,50,50);\n"
            "font-size: 13pt;")

    def signUpSeq(self,event):
        if (self.idCheckFlag == True) and (self.ui.signUpLineEditList[2].text() == self.ui.signUpLineEditList[3].text()) and self.ui.signUpLineEditList[2].text() != "":
            db = DataBase()
            colTemp = ("id","pw","name")
            dataTemp = (self.ui.signUpLineEditList[0].text(),self.ui.signUpLineEditList[2].text(),self.ui.signUpLineEditList[1].text())
            db.dataCreate("user",colTemp,dataTemp)
            #필요 없으면 삭제
            mb = QtWidgets.QMessageBox(self.ui.pageList[0])
            mb.setStyleSheet("color: white;")
            mb.setText("가입을 환영합니다!")
            mb.show()
            self.showSignIn()
        else:
            self.ui.signUpCheckLabel.setText("Wrong!")

    def goToSignIn(self,event):
        self.showSignIn()
        
    def showSignIn(self):
        self.ui.signUpLineEditList[0].setDisabled(False)
        self.ui.idCheckLabel.setText("")
        self.ui.signUpCheckLabel.setText("")
        for i in range(0,4):
            self.ui.signUpLineEditList[i].setText("")
        self.ui.stackedWidget.setCurrentIndex(0)
        for i in range(0,3):
            self.ui.signUpBtnList[i].disconnect()