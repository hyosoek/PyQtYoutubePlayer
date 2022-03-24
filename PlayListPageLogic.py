import sys
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
        self.playListData = db.dataRead("playlist","usercode",self.usercode)
        self.userData = db.dataRead("user","usercode",self.usercode)

        for i in range(0,len(self.playListData)):
            self.addPlayList(self.playListData[i][1])

        self.ui.playListidLabel.setText(self.userData[0][0]+"님 환영합니다!")


        self.ui.playListBtnList[0].clicked.connect(lambda event: self.showSignIn(event))
        self.ui.playListBtnList[1].clicked.connect(lambda event: self.addPlayListSeq(event))
              


    def addPlayListSeq(self,event):
        db = DataBase() #data create에 필요
        namecheck = False
        playListName, ok = QInputDialog.getText(self, 'Add PlayList', "PlayList's Name")
        if ok:
            for i in range(0,len(self.playListData)):
                if  self.playListData[0][1] == playListName:
                    namecheck = True
            if namecheck == False:
                colTemp = ("usercode","playlistname")
                dataTemp = (self.usercode,playListName)
                db.dataCreate("playlist",colTemp,dataTemp)
                self.addPlayList(playListName)
            else:
                pass



    def addPlayList(self,playListName):
        playListBtn = QtWidgets.QWidget()
        playListBtn.setFixedWidth(500)
        playListBtn.setFixedHeight(100)
        playListBtn.setStyleSheet("background-color : rgb(30,30,30);\n"
                "border-radius: 8px;\n")
        
        for i in range(0,len(self.playListData)): #플레이리스트 조회
            if(self.playlistData[i][1] == playListName):
                playlistcode = self.playlistData[i][2] #플레이리스트 코드 저장
        
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
        db = DataBase
        for i in range(0,len(self.playListData)):
            if self.playListData[i][1] == playListName:
                playListCode = self.playListData[i][2]
        videoDataTemp = db.dataRead("video","playlistcode",playListCode) #앞에서 호출하나 뒤에서 호출하나 한번함.
        for i in range(0,len(videoDataTemp)):
            db.dataDelete("video","videocode",videoDataTemp[i][2]) #어차피 삭제해야함
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