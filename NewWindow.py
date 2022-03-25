import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from Ui import *
from DataBase import *
from VideoPageLogic import *


class NewWindow(QWidget):
    def __init__(self):
         super(NewWindow, self).__init__()
         self.resize(400, 300)

         # Label
         self.label = QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('Sub Window')
         self.label.setAlignment(Qt.AlignCenter)
         self.label.setStyleSheet('font-size:40px')
