import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import pyqtSignal, QObject
from Ui import *
from DataBase import *
from NewWindow import *
import pafy
#영상 재생을 위해서
import threading
import time


class VideoPageLogic(QObject,threading.Thread):
    signal = pyqtSignal(int)

    def __init__(self,Ui,playListCode,userName):
        super().__init__()

        self.ui = Ui
        self.playListCode = playListCode
        self.videoBtnList = []
        self.videlDelBtnList = []
        self.videoNameLabelList = []
        self.videoThumbNailList = []

        db = DataBase()
        self.videoData = db.dataRead("video","playlistcode",self.playListCode)
        self.playListData = db.dataRead("playlist","playlistcode",self.playListCode)

        for i in range(0,len(self.videoData)): 
            self.addVideo(self.videoData[i][2]) #parameter로 url을 사용하지 않습니다.
        self.start()
        self.ui.videoPageidLabel.setText(userName+"님 환영합니다!")
        self.ui.videoPageBtnList[0].clicked.connect(lambda event: self.showPlayList(event))
        self.ui.videoPageBtnList[1].clicked.connect(lambda event: self.addVideoSeq(event))
        self.signal.connect(self.videoBtnSubWidget)

    def run(self):
        self.signal.emit(44)

    def addVideoSeq(self,event):
        self.newAddWindow = NewWindow()
        self.newAddWindow.addPlayList()
        self.newAddWindow.show()
        self.newAddWindow.cancelBtn.clicked.connect(lambda event: self.cancelBtnSeq(event))
        self.newAddWindow.enrollBtn.clicked.connect(lambda event: self.enrollBtnSeq(event))

    def enrollBtnSeq(self,event): #가장먼저 중복처리 후 url 등록시도
        flag = False
        try: #유효한 url인가?
            url = self.newAddWindow.inputLineEdit.text()
            video = pafy.new(url)

            for i in range(0,len(self.videoData)):
                if self.newAddWindow.inputLineEdit.text() == self.videoData[i][1]: #url 체크
                    flag = True
            if flag == True: #중복된 아이디가 있으면
                    self.newAddWindow.warnLabel.setText("Invalid!")
            else:
                db = DataBase()
                colTemp = ("playlistcode","url")
                dataTemp = (self.playListCode, url)
                db.dataCreate("video",colTemp,dataTemp)
                self.videoData = db.dataRead("video","playlistcode",self.playListCode)
                videoCode = self.videoData[len(self.videoData)-1][2]
                print(self.videoData)
                self.addVideo(videoCode)
                self.closeAddWindow()
        except:
            self.newAddWindow.warnLabel.setText("Invalid!")
        
    def cancelBtnSeq(self,event):
        self.closeAddWindow()

    def closeAddWindow(self):
        self.newAddWindow.cancelBtn.disconnect()
        self.newAddWindow.enrollBtn.disconnect()
        self.newAddWindow.close()
        del self.newAddWindow

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
        #videoBtn.mouseReleaseEvent = lambda event: self.loadVideo(event,videoUrl) #url에 접근할때만 사용합니다.

        #영상삭제버튼
        delBtn = QtWidgets.QLabel(videoBtn)
        delBtn.setGeometry(QtCore.QRect(220, 60, 30, 30))
        delBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
        " font-size : 25pt;\n"
        " color : white;\n"
        "padding-left : 1px;")
        delBtn.setText("X")
        delBtn.mouseReleaseEvent = lambda event: self.removeVideoSeq(event,videocode)

        self.videoBtnList.append(videoBtn)
        self.videlDelBtnList.append(delBtn)
        #self.videoBtnSubWidget(videocode)


    def videoBtnSubWidget(self,videocode): 
        for i in range(0,len(self.videoData)):
            if self.videoData[i][2] == videocode:
                url = self.videoData[i][1]
                index = i
        video = pafy.new(url)        

        videoThumbNailUrl  = video.thumb
        image = QImage()
        image.loadFromData(requests.get(videoThumbNailUrl).content)
        thumbNail = QtWidgets.QLabel(self.videoBtnList[index])
        thumbNail.setPixmap(QPixmap(image))
        thumbNail.setGeometry(QtCore.QRect(-50, 10, 200, 80))
        
        
        self.videoNameLabel = QtWidgets.QLabel(self.videoBtnList[index])
        self.videoNameLabel.setStyleSheet("background-color : rgb(30,30,30);\n"
                "color : white;\n"
                "padding-left : 0px;\n"
                "font-size: 12pt;")
        self.videoNameLabel.setGeometry(QtCore.QRect(140, 3, 140, 50))

        newLinedTitle = ""
        oldTitle = video.title
        for i in range(0,len(oldTitle)):
            if i%13 == 12:
                newLinedTitle += oldTitle[i]
                newLinedTitle += "\n"
            else:
                newLinedTitle += oldTitle[i]
        self.videoNameLabel.setText(newLinedTitle)
        self.videoThumbNailList.append(thumbNail)
        self.videoNameLabelList.append(self.videoNameLabel)
                    

    def removeVideoSeq(self,event,videoCode): #여기에 묻는 창 만들기
        self.newDelWindow = NewWindow()
        self.newDelWindow.delConfirm()
        self.newDelWindow.show()
        self.newDelWindow.noBtn.clicked.connect(lambda event: self.noBtnSeq(event))
        self.newDelWindow.yesBtn.clicked.connect(lambda event, videoCode_ = videoCode: self.yesBtnSeq(event,videoCode_))

    def yesBtnSeq(self,event,videoCode):
        self.delVideo(videoCode)
        self.closeDelWindow()

    def noBtnSeq(self,event):
        self.closeDelWindow()
    
    def closeDelWindow(self):
        self.newDelWindow.noBtn.disconnect()
        self.newDelWindow.yesBtn.disconnect()
        del self.newDelWindow

    def delVideo(self,videoCode): #비디오 코드 조회해서 삭제하기
        db = DataBase()
        db.dataDelete("video","videocode",videoCode)
        for i in range(0,len(self.videoBtnList)):
            if (self.videoBtnList[i].objectName() == str(videoCode)):
                delIndex = i
        self.videoBtnList[delIndex].deleteLater()
        del self.videoBtnList[delIndex]
        del self.videoData[delIndex] #그래야 방금 지운거 다시 추가 할 수 있음.
        
        
    def loadVideo(self,url):
        pass

    def showPlayList(self,event):
        self.ui.stackedWidget.setCurrentIndex(2)
        for i in range(0,2):
            self.ui.videoPageBtnList[i].disconnect()
        for i in range(0,len(self.videoBtnList)):
            self.videoBtnList[i].disconnect()
            self.videoBtnList[i].deleteLater()
        del self.videoBtnList
        del self.videlDelBtnList
        del self.videoNameLabelList


