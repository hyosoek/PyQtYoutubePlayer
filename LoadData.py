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

        video = pafy.new(url)        
        videoThumbNailUrl  = video.thumb
        image = QImage()
        image.loadFromData(requests.get(videoThumbNailUrl).content)
        

        newLinedTitle = ""
        oldTitle = video.title
        for j in range(0,len(oldTitle)):
            if j%13 == 12:
                newLinedTitle += oldTitle[j]
                newLinedTitle += "\n"
            else:
                newLinedTitle += oldTitle[j]
        
        thumbNail.setPixmap(QPixmap(image))
        videoNameLabel.setText(newLinedTitle)
            


    