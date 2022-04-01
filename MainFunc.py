from SignInPageLogic import *
from Ui import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PlayListPageLogic import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    signIn = SignInPageLogic()
    sys.exit(app.exec_())
