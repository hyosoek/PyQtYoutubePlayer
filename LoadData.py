import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import pyqtSignal, QObject
from Ui import *
from DataBase import *

import pafy
import threading

class LoadData(QObject,threading.Thread):
    def __init__(self,url,thumbNail,videoNameLabel):
        super().__init__()
        self.url = url
        self.thumbNail = thumbNail
        self.videoNameLabel = videoNameLabel
        self.start()

        self.errorExist = False 
        self.videoPlayData = None
        self.oldtitle = None

    def run(self):
        try:            
            video = pafy.new(self.url)                                                                                                 
            best = video.getbest()                                                                                                                 
            playurl = best.url
            self.videoPlayData = playurl 

            videoThumbNailUrl  = video.thumb
            image = QImage()
            image.loadFromData(requests.get(videoThumbNailUrl).content)
            
            newLinedTitle = ""
            oldTitle = video.title
            self.oldtitle = oldTitle
            for j in range(0,len(oldTitle)):
                if j%13 == 12:
                    newLinedTitle += oldTitle[j]
                    newLinedTitle += "\n"
                else:
                    newLinedTitle += oldTitle[j]
            
            self.thumbNail.setPixmap(QPixmap(image))
            self.videoNameLabel.setText(newLinedTitle)


        except:
            print("??")
            self.errorExist = True
            
                


    