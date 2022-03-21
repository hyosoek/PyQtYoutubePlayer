import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
#삭제할 것들
from PyQt5.QtGui import QImage, QPixmap
import requests

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : black;")
        self.setFixedSize(1600, 900)
        self.centralWidget = QtWidgets.QWidget(self)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.pageList = []
        for i in range(0,4):
            page = QtWidgets.QWidget()
            self.pageList.append(page)
            self.stackedWidget.addWidget(self.pageList[i])
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.signInPageUi()
        self.signUpPageUi()
        self.playListPageUi()
        self.videoPageUi()
        self.setCentralWidget(self.centralWidget)
        self.show()


    def signInPageUi(self):
        self.signIpBtnList = []
        btn = QtWidgets.QPushButton(self.pageList[0])
        btn.setGeometry(QtCore.QRect(650,640,300,50))
        btn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "border-radius: 5px;\n"
                "color : white;"
                "font-size: 20pt;")
        btn.setText("Sign In")
        self.signIpBtnList.append(btn)

        btn = QtWidgets.QPushButton(self.pageList[0])
        btn.setGeometry(QtCore.QRect(600,820,400,30))
        btn.setStyleSheet("border-radius: 5px;\n"
                "color : white;"
                "font-size: 16pt;")
        btn.setText("Don't have an ID? click here to Sign Up")
        self.signIpBtnList.append(btn)    
        
        self.signInLineEditList = []
        for i in range(0,2):
                lineEdit = QtWidgets.QLineEdit(self.pageList[0])
                lineEdit.setGeometry(QtCore.QRect(650,510+60*i,300,50))
                lineEdit.setStyleSheet(
                    "background-color : rgb(50,50,50);"
                    "padding-left : 20px;"
                    "border-radius: 5px;"
                    "font-size: 16pt;"
                    "color : white;")
                self.signInLineEditList.append(lineEdit)
        self.signInLineEditList[0].setPlaceholderText("User ID")
        self.signInLineEditList[1].setPlaceholderText("PassWord")
        self.signInLineEditList[1].setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.idWrongLabel = QtWidgets.QLabel(self.pageList[0])
        self.idWrongLabel.setGeometry(QtCore.QRect(900, 620, 60, 20))
        self.idWrongLabel.setText("")
        self.idWrongLabel.setStyleSheet("color: red;\n"
            "font-size: 13pt;")

        logoImage = QtWidgets.QPushButton(self.pageList[0])
        logoImage.setGeometry(QtCore.QRect(675,180,250,250))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stageUsLogo.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        logoImage.setIcon(icon)
        logoImage.setIconSize(QtCore.QSize(250, 250))

        
        
         

    def signUpPageUi(self):
        self.signUpBtnList = []
        signUpBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpBtn.setGeometry(QtCore.QRect(650,540,300,50))
        signUpBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "border-radius: 5px;\n"
                "color : white;"
                "font-size: 20pt;")
        signUpBtn.setText("Sign In")
        self.signUpBtnList.append(signUpBtn)

        signUpCheckBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpCheckBtn.setGeometry(QtCore.QRect(870,280,80,50))
        signUpCheckBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 5px;\n"
                "color : white;\n"
                "font-size: 13pt;")
        signUpCheckBtn.setText("Check")
        self.signUpBtnList.append(signUpCheckBtn)

        signUpBackBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpBackBtn.setGeometry(QtCore.QRect(1450,20,113,32))
        signUpBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 10px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        signUpBackBtn.setText("< Back")
        self.signUpBtnList.append(signUpBackBtn)   
        

        self.signUpLineEditList = []
        lineEdit = QtWidgets.QLineEdit(self.pageList[1])
        lineEdit.setGeometry(QtCore.QRect(650,280,215,50))
        lineEdit.setStyleSheet(
            "background-color : rgb(50,50,50);"
            "padding-left : 20px;"
            "border-radius: 5px;"
            "font-size: 20pt;"
            "color : white;")
        self.signUpLineEditList.append(lineEdit)

        for i in range(0,3):
                lineEdit = QtWidgets.QLineEdit(self.pageList[1])
                lineEdit.setGeometry(QtCore.QRect(650,340+60*i,300,50))
                lineEdit.setStyleSheet(
                    "background-color : rgb(50,50,50);"
                    "padding-left : 20px;"
                    "border-radius: 5px;"
                    "font-size: 20pt;"
                    "color : white;")
                self.signUpLineEditList.append(lineEdit)

        self.signUpLineEditList[0].setPlaceholderText("User ID")
        self.signUpLineEditList[1].setPlaceholderText("Name")
        self.signUpLineEditList[2].setPlaceholderText("PassWord")
        self.signUpLineEditList[3].setPlaceholderText("PassWord Check")
        for i in range(0,2):
            self.signUpLineEditList[i+2].setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.idCheckLabel = QtWidgets.QLabel(self.pageList[1])
        self.idCheckLabel.setGeometry(QtCore.QRect(810, 295, 45, 20))
        self.idCheckLabel.setText("")
        self.idCheckLabel.setStyleSheet(
            "background-color : rgb(50,50,50);\n"
            "font-size: 13pt;")

        self.signUpCheckLabel = QtWidgets.QLabel(self.pageList[1])
        self.signUpCheckLabel.setGeometry(QtCore.QRect(870,515,80,20))
        self.signUpCheckLabel.setText("")
        self.signUpCheckLabel.setStyleSheet(
            "background-color : black;\n"
            "color : red;\n"
            "font-size: 13pt;")
         
    


    def playListPageUi(self):

        self.playListScroll = QtWidgets.QScrollArea(self.pageList[2])
        self.playListWidget = QtWidgets.QWidget()
        self.playListVbox = QtWidgets.QVBoxLayout() 

        self.playListScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.playListScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.playListScroll.setWidgetResizable(True)
        self.playListScroll.setGeometry(QtCore.QRect(550,100,540,800))

        
        self.playListWidget.setLayout(self.playListVbox)
        self.playListScroll.setWidget(self.playListWidget)


        self.playListidLabel = QtWidgets.QLabel(self.pageList[2])
        self.playListidLabel.setGeometry(QtCore.QRect(50, 20, 140, 20))
        self.playListidLabel.setStyleSheet(
                "color : white;"
                "font-size: 13pt;")
        self.playListidLabel.setText("님 환영합니다!")

        self.playListBtnList = []
        playListBackBtn = QtWidgets.QPushButton(self.pageList[2])
        playListBackBtn.setGeometry(QtCore.QRect(1450,20,113,32))
        playListBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 4px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        playListBackBtn.setText("< Back")
        self.playListBtnList.append(playListBackBtn)   

        playListAddBtn = QtWidgets.QPushButton(self.pageList[2])
        playListAddBtn.setGeometry(QtCore.QRect(1320,20,113,32))
        playListAddBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "padding-left : 2px;\n"
                "font-size: 13pt;\n"
                "border-radius: 4px;\n"
                "color : white;")
        playListAddBtn.setText("+ Add PlayList")
        self.playListBtnList.append(playListAddBtn)



    def videoPageUi(self):
        #스크롤
        self.videoScroll = QtWidgets.QScrollArea(self.pageList[3])
        self.videoListWidget = QtWidgets.QWidget()
        self.videoListVbox = QtWidgets.QVBoxLayout() 

        self.videoScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.videoScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.videoScroll.setWidgetResizable(True)
        self.videoScroll.setGeometry(QtCore.QRect(1290,60,300,800))

        self.videoListWidget.setLayout(self.videoListVbox)
        self.videoScroll.setWidget(self.videoListWidget)

        #중복코드 인가?
        self.videoPageidLabel = QtWidgets.QLabel(self.pageList[3])
        self.videoPageidLabel.setGeometry(QtCore.QRect(50, 20, 140, 20))
        self.videoPageidLabel.setStyleSheet(
                "color : white;"
                "font-size: 13pt;")
        self.videoPageidLabel.setText("님 환영합니다!")

        self.videoPageBtnList = []
        videoPageBackBtn = QtWidgets.QPushButton(self.pageList[3])
        videoPageBackBtn.setGeometry(QtCore.QRect(1450,20,113,32)) #1450
        videoPageBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 4px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        videoPageBackBtn.setText("< Back")
        self.videoPageBtnList.append(videoPageBackBtn)   

        videoAddBtn = QtWidgets.QPushButton(self.pageList[3])
        videoAddBtn.setGeometry(QtCore.QRect(1320,20,113,32))
        videoAddBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "padding-left : 2px;\n"
                "font-size: 13pt;\n"
                "border-radius: 4px;\n"
                "color : white;")
        videoAddBtn.setText("+ Add Video")
        self.videoPageBtnList.append(videoAddBtn)


        #영상 하단바
        self.TitleLabel = QtWidgets.QLabel(self.pageList[3])
        self.TitleLabel.setGeometry(QtCore.QRect(40, 840, 850, 40))
        self.TitleLabel.setStyleSheet(
                "color : white;"
                "font-size: 25pt;")
        self.TitleLabel.setText("Vidoe Title")

        self.videoWidget = QtWidgets.QWidget(self.pageList[3])
        self.videoWidget.setGeometry(QtCore.QRect(10, 50, 1280, 720))
        self.videoWidget.setStyleSheet("background-color : rgb(80,80,80);")

        self.volumeSlider = QtWidgets.QSlider(Qt.Horizontal, self.pageList[3])
        self.volumeSlider.move(30, 30)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setSingleStep(1)
        self.volumeSlider.setGeometry(10, 785, 110, 40)

        self.videoControlBtnList = []
        imageList  = ("play.png","pause.png","stop.png")
        for i in range(0,3):
            controlBtn = QtWidgets.QPushButton(self.pageList[3])
            controlBtn.setGeometry(QtCore.QRect(570+ 50 * i, 785, 40, 40))
            self.videoControlBtnList.append(controlBtn)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(imageList[i]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.videoControlBtnList[i].setIcon(icon)
            self.videoControlBtnList[i].setIconSize(QtCore.QSize(40, 40))
            