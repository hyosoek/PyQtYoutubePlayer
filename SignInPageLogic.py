import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
from SignUpPageLogic import *
from PlayListPageLogic import *

class SignInPageLogic:
    def __init__(self):
        self.ui = Ui()
        self.ui.signIpBtnList[0].clicked.connect(lambda event: self.signInSequence(event))
        self.ui.signIpBtnList[1].clicked.connect(lambda event: self.showSignUp(event))
        self.ui.signIpBtnList[0].enterEvent = lambda event : self.signInBtnColorChange1(event)
        self.ui.signIpBtnList[0].leaveEvent = lambda event : self.signInBtnColorChange2(event)
        self.ui.signIpBtnList[1].enterEvent = lambda event : self.goToSignUpBtnColorChange1(event)
        self.ui.signIpBtnList[1].leaveEvent = lambda event : self.goToSignUpBtnColorChange2(event)

    def signInSequence(self,event):
        db = DataBase()
        userDataTemp = db.dataRead("user","","") #확인을 눌러줄때마다 db정보를 새로 갱신합니다.
        idtemp = self.ui.signInLineEditList[0].text()
        pwtemp = self.ui.signInLineEditList[1].text()
        userIndex = -1
        for i in range(0,len(userDataTemp)):
            if userDataTemp[i][0] == idtemp:
                userIndex = i
        if idtemp == "" or pwtemp == "" or userIndex == -1 or (userDataTemp[userIndex][1] != pwtemp):
            self.ui.idWrongLabel.setText("Wrong!")
        else:
            self.showPlayList(userDataTemp[userIndex][3])


    def showPlayList(self,usercode):
        for i in range(0,2):
            self.ui.signInLineEditList[i].setText("")
        self.ui.idWrongLabel.setText("")
        self.ui.stackedWidget.setCurrentIndex(2)
        self.playList = PlayListPageLogic(self.ui,usercode)
        

    def showSignUp(self,event):
        for i in range(0,2):
            self.ui.signInLineEditList[i].setText("")
        self.ui.idWrongLabel.setText("")

        self.ui.stackedWidget.setCurrentIndex(1)
        self.signUp = SignUpPageLogic(self.ui)


    #design Func
    def signInBtnColorChange1(self,event):
        styleSheet = self.ui.signIpBtnList[0].styleSheet()
        styleSheet += "background-color : rgb(180,0,0);"
        self.ui.signIpBtnList[0].setStyleSheet(styleSheet)

    def signInBtnColorChange2(self,event):
        styleSheet = self.ui.signIpBtnList[0].styleSheet()
        styleSheet += "background-color : rgb(220,0,0);"
        self.ui.signIpBtnList[0].setStyleSheet(styleSheet)

    def goToSignUpBtnColorChange1(self,event):
        styleSheet = self.ui.signIpBtnList[1].styleSheet()
        styleSheet += "color : rgb(200,200,200);"
        self.ui.signIpBtnList[1].setStyleSheet(styleSheet)

    def goToSignUpBtnColorChange2(self,event):
        styleSheet = self.ui.signIpBtnList[1].styleSheet()
        styleSheet += "color : white;"
        self.ui.signIpBtnList[1].setStyleSheet(styleSheet)