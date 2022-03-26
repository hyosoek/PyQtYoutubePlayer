import sys
from PyQt5.QtWidgets import *
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
import pafy
#영상 재생을 위해서
import threading


class VideoPageLogic(QWidget):
    def __init__(self,Ui,playListCode,userName):
        super().__init__()
        self.ui = Ui
        self.playListCode = playListCode
        self.videoBtnList = []
        self.videlDelBtnList = []
        # self.videoNameLabelList = []
        # self.thubNailList = []

        db = DataBase()
        self.videoData = db.dataRead("video","playlistcode",self.playListCode)

        for i in range(0,len(self.videoData)): 
            self.addVideo(self.videoData[i][2]) #parameter로 url을 사용하지 않습니다.

        self.playListData = db.dataRead("playlist","playlistcode",self.playListCode)
        
        self.ui.videoPageidLabel.setText(userName+"님 환영합니다!")

        self.ui.videoPageBtnList[0].clicked.connect(lambda event: self.showPlayList(event))
        self.ui.videoPageBtnList[1].clicked.connect(lambda event: self.addVideoSeq(event))

##############################################################################################################

    def addVideoSeq(self,event):
        db = DataBase() 
        url, ok = QInputDialog.getText(self, 'Add Video', "what is Video URL?")
        #한 유저 내 url 중복체크 기능이 필요합니다.
        if ok:
            colTemp = ("playlistcode","url")
            dataTemp = (self.playListCode,url)
            db.dataCreate("video",colTemp,dataTemp)
            videoData = db.dataRead("video","playlistcode",self.playListCode) 
            for i in range(0,len(videoData)):
                if videoData[i][1] == url:
                    videocode = videoData[i][2]
            self.addVideo(videocode)
##############################################################################################################


    def addVideo(self,videocode):
        #영상버튼
        videoBtn = QtWidgets.QWidget()
        videoBtn.setFixedWidth(260)
        videoBtn.setFixedHeight(100)
        videoBtn.setStyleSheet("background-color : rgb(30,30,30);\n"
                "color : white;\n"
                "padding-left:60px;\n"
                "border-radius: 8px;")
        self.ui.videoListVbox.addWidget(videoBtn)
        videoBtn.setObjectName(str(videocode)) #버튼에 비디오 코드로 값을 매겨주면 접근이 편합니다.
        
        for i in range(0,len(self.videoData)):
            if self.videoData[i][2] == videocode:
                videoUrl = self.videoData[i][1]
        #videoBtn.mouseReleaseEvent = lambda event: self.loadVideo(event,videoUrl) #url에 접근할때만 사용합니다.

        #영상삭제버튼
        delBtn = QtWidgets.QWidget(videoBtn)
        delBtn.setGeometry(QtCore.QRect(220, 60, 30, 30))
        delBtn.setStyleSheet("background-color : rgb(80,80,80);\n")
        delBtn.mouseReleaseEvent = lambda event: self.removeVideo(event,videoUrl)
        
        # 영상썸네일
        # url = videoUrl
        # video = pafy.new(url)
        # videoThumbNailUrl  = video.thumb
        # image = QImage()
        # image.loadFromData(requests.get(videoThumbNailUrl).content)
        # thumbNail = QtWidgets.QLabel(videoBtn)
        # thumbNail.setPixmap(QPixmap(image))
        # thumbNail.setGeometry(QtCore.QRect(-50, 10, 200, 80))
        
        # #영상제목
        # videoNameLabel = QtWidgets.QLabel(videoBtn)
        # videoNameLabel.setStyleSheet("background-color : rgb(30,30,30);\n"
        #         "color : white;\n"
        #         "padding-left : 0px;\n"
        #         "font-size: 12pt;")
        # videoNameLabel.setGeometry(QtCore.QRect(140, 5, 120, 50))
        
        # newLinedTitle = ""
        # oldTitle = video.title
        # for i in range(0,len(oldTitle)):
        #     if i%13 == 12:
        #         newLinedTitle += oldTitle[i]
        #         newLinedTitle += "\n"
        #     else:
        #         newLinedTitle += oldTitle[i]
               
        # videoNameLabel.setText(newLinedTitle)
        
        
        #모든 위젯을 관리해줄 list
        self.videoBtnList.append(videoBtn)
        self.videlDelBtnList.append(delBtn)
        # self.videoNameLabelList.append(videoNameLabel)
        # self.thubNailList.append(thumbNail)


    def removeVideo(self,event,url):
        db = DataBase()
        for i in range(0,len(self.videoData)):
            if self.videoData[i][1] == url:
                videoCode = self.videoData[i][2]
        db.dataDelete("video","videocode",videoCode)

        for i in range(0,len(self.videoBtnList)):
            if (self.videoBtnList[i].objectName() == str(videoCode)):
                delIndex = i
        self.videoBtnList[delIndex].deleteLater()
        del self.videoBtnList[delIndex]
        self.videlDelBtnList[delIndex].deleteLater()
        del self.videlDelBtnList[delIndex]
        # self.videoNameLabelList[delIndex].deleteLater()
        # del self.videoNameLabelList[delIndex]

    def loadVideo(self,url):
        pass

    def showPlayList(self,event):
        self.ui.stackedWidget.setCurrentIndex(2)
        for i in range(0,2):
            self.ui.videoPageBtnList[i].disconnect()
        for i in range(0,len(self.videoBtnList)):
            #self.videoBtnList[i].disconnect()
            #self.videlDelBtnList[i].disconnect()
            self.videoBtnList[i].deleteLater()
            self.videlDelBtnList[i].deleteLater()
            # self.videoNameLabelList[i].deleteLater()

        del self.videoBtnList
        del self.videlDelBtnList
        # del self.videoNameLabelList


