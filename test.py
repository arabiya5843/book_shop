import sys
from PyQt5.QtWidgets import *
from main import Login_window, Shop_window

if __name__ == '__main__':

    App = QApplication(sys.argv)

    login_window = Login_window()
    login_window.showMaximized()

    if login_window.exec_() == QDialog.Accepted:
        window = Shop_window()
        window.showMaximized()

    else:
        login_window.close()

    sys.exit(App.exec())










