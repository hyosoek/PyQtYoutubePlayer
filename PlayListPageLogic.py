import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
from VideoPageLogic import *
from NewWindow import *

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
            self.addPlayList(self.playListData[i][2])
            
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
                
    # def addPlayListSeq(self,event):
    #     self.newWindow = NewWindow()
    #     self.newWindow.addPlayList()
    #     self.newWindow.show()
        #db add해주고, playListData도 데이터 한번 업데이트 해주기


    def addPlayList(self,playListCode):

        playListBtn = QtWidgets.QWidget()
        playListBtn.setFixedWidth(500)
        playListBtn.setFixedHeight(100)
        playListBtn.setStyleSheet("background-color : rgb(30,30,30);\n"
                "border-radius: 8px;\n")
        playListBtn.setObjectName(str(playListCode))
        playListBtn.mouseReleaseEvent = lambda event: self.showVideoPage(event,playListCode) 

        playListLabel = QtWidgets.QLabel(playListBtn)
        playListLabel.setGeometry(QtCore.QRect(210, 25, 100, 50))
        playListLabel.setStyleSheet("background-color : rgb(30,30,30);\n"
                "color : white;\n"
                "font-size: 25pt;")
        for i in range(0,len(self.playListData)):
            if self.playListData[i][2] == playListCode:
                playListLabel.setText(self.playListData[i][1])

        delBtn = QtWidgets.QLabel(playListBtn)
        delBtn.setGeometry(QtCore.QRect(450, 10, 40, 80))
        delBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
        " font-size : 30pt;\n"
        " color : white;\n"
        "padding-left : 4px;")
        delBtn.setText("X")
        delBtn.mouseReleaseEvent = lambda event, code = playListCode: self.removePlayList(event,code)#등록당시의 버튼 크기가 아닌 것으로 등록됨

        self.ui.playListVbox.addWidget(playListBtn)
        self.playListBtnList.append(playListBtn)
        self.playListDelBtnList.append(delBtn)
        self.playListLabelList.append(playListLabel)

    def removeSeq(self,event,code): #물어보는 부분
        self.newWindow = NewWindow()
        self.newWindow.delConfirm()
        self.newWindow.show()

    def removePlayList(self,event,playListCode):
        db = DataBase()
        db.dataDelete("video","playlistcode",playListCode) #어차피 삭제해야함
        db.dataDelete("playlist","playlistcode",playListCode)
        for i in range(0,len(self.playListLabelList)):
            if (self.playListBtnList[i].objectName() == str(playListCode)):
                delIndex = i
        self.playListDelBtnList[delIndex].deleteLater()
        del self.playListDelBtnList[delIndex]
        self.playListBtnList[delIndex].deleteLater()
        del self.playListBtnList[delIndex]
        self.playListLabelList[delIndex].deleteLater()
        del self.playListLabelList[delIndex]
        

    def showVideoPage(self,event,playListCode):
        self.videoPage = VideoPageLogic(self.ui,playListCode,self.userData[0][0])
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