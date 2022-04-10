import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

from PyQt5 import QtCore
class MainWindows(QMainWindow):
    
    def __init__(self):
        super(MainWindows, self).__init__()
        self.setWindowTitle("BROWSER")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        thing = QToolBar()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.addToolBar(thing)
        
     
        back = QAction("Back",self)
        back.triggered.connect(self.browser.back)
        thing.addAction(back)
        back.setIcon(QtGui.QIcon("back.png"))
    

        forward = QAction("Forward",self)
        forward.triggered.connect(self.browser.forward)
        thing.addAction(forward)
        forward.setIcon(QtGui.QIcon("forward.png"))

        reload = QAction("Reload",self)
        reload.triggered.connect(self.browser.reload)
        thing.addAction(reload)
        reload.setIcon(QtGui.QIcon("reload.png"))

        home = QAction("Home",self)
        home.triggered.connect(self.navigate_home)
        thing.addAction(home)
        home.setIcon(QtGui.QIcon("home.png"))
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        thing.addWidget(self.url_bar)
      

        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())

        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    QApplication.setApplicationName('Copy Assignments Browser')
    window = MainWindows()
    app.setStyle("Fusion")
    app.exec_()
