import sys
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
from VideoPageLogic import *

class PlayListPageLogic(QWidget):
    def __init__(self,Ui,usercode):
        super().__init__()
        self.ui = Ui
        
        self.usercode = usercode
        self.playListBtnList = []
        self.playListDelBtnList = []
        self.playListLabelList = []
        db = DataBase()
        playListData = db.dataRead("playlist","usercode",self.usercode)
        for i in range(0,len(playListData)):
            self.addPlayList(playListData[i][1])
        userData = db.dataRead("user","usercode",self.usercode)
        self.ui.playListidLabel.setText(userData[0][0]+"님 환영합니다!")


        self.ui.playListBtnList[0].clicked.connect(lambda event: self.showSignIn(event))
        self.ui.playListBtnList[1].clicked.connect(lambda event: self.addPlayListSeq(event))
              


    def addPlayListSeq(self,event):
        db = DataBase()
        playListName, ok = QInputDialog.getText(self, 'Add PlayList', "PlayList's Name")
        #한 유저 내 playList 중복체크 기능이 필요합니다.
        if ok:
            colTemp = ("usercode","playlistname")
            dataTemp = (self.usercode,playListName)
            db.dataCreate("playlist",colTemp,dataTemp)
            self.addPlayList(playListName)



    def addPlayList(self,playListName):
        playListBtn = QtWidgets.QWidget()
        playListBtn.setFixedWidth(500)
        playListBtn.setFixedHeight(100)
        playListBtn.setStyleSheet("background-color : rgb(30,30,30);\n"
                "border-radius: 8px;\n")
        db = DataBase()
        playlistData = db.dataRead("playlist","usercode",self.usercode) #유저코드 조회
        for i in range(0,len(playlistData)): #플레이리스트 조회
            if(playlistData[i][1] == playListName):
                playlistcode = playlistData[i][2] #플레이리스트 코드 저장
        
        playListBtn.mouseReleaseEvent = lambda event: self.showVideoPage(event,playlistcode) 

        playListLabel = QtWidgets.QLabel(playListBtn)
        playListLabel.setGeometry(QtCore.QRect(210, 25, 100, 50))
        playListLabel.setStyleSheet("background-color : rgb(30,30,30);\n"
                "color : white;\n"
                "font-size: 25pt;")
        playListLabel.setText(playListName)

        delBtn = QtWidgets.QWidget(playListBtn)
        delBtn.setGeometry(QtCore.QRect(450, 10, 40, 80))
        delBtn.setStyleSheet("background-color : rgb(80,80,80);\n")
        
        #delBtn.mouseReleaseEvent = lambda event, playListName_ = playListName: self.removePlayList(event,playListName_)
        delBtn.mouseReleaseEvent = lambda event: self.removePlayList(event,playListName)#등록당시의 버튼 크기가 아닌 것으로 등록됨

        self.ui.playListVbox.addWidget(playListBtn)
        self.playListBtnList.append(playListBtn)
        self.playListDelBtnList.append(delBtn)
        self.playListLabelList.append(playListLabel)



    def removePlayList(self,event,playListName):
        db = DataBase()
        playListDataTemp = db.dataRead("playlist","usercode",self.usercode)
        for i in range(0,len(playListDataTemp)):
            if playListDataTemp[i][1] == playListName:
                playListCode = playListDataTemp[i][2]
        videoDataTemp = db.dataRead("video","playlistcode",playListCode)
        for i in range(0,len(videoDataTemp)):
            db.dataDelete("video","videocode",videoDataTemp[i][2])

        
        db.dataDelete("playlist","playlistcode",playListCode)

        for i in range(0,len(self.playListLabelList)):
            if (self.playListLabelList[i].text() == playListName):
                delIndex = i
        self.playListDelBtnList[delIndex].deleteLater()
        del self.playListDelBtnList[delIndex]
        self.playListBtnList[delIndex].deleteLater()
        del self.playListBtnList[delIndex]
        self.playListLabelList[delIndex].deleteLater()
        del self.playListLabelList[delIndex]
        



    def showVideoPage(self,event,playListCode):
        self.videoPage = VideoPageLogic(self.ui,playListCode)
        self.ui.stackedWidget.setCurrentIndex(3)



    def showSignIn(self,event):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.playListBtnList[0].disconnect()
        self.ui.playListBtnList[1].disconnect()
        for i in range(0,len(self.playListBtnList)):
            self.playListBtnList[i].disconnect()
            self.playListDelBtnList[i].disconnect()
            self.playListBtnList[i].deleteLater()
            self.playListLabelList[i].deleteLater()
            self.playListDelBtnList[i].deleteLater()
        del self.playListBtnList
        del self.playListLabelList
        del self.playListDelBtnList
            


    def modifyBtnDesign(self,event):
        pass