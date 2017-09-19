# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:27:14 2017

@author: e115487
"""




# import * frowned upon but works in this case
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# import sys
import sys

# Class window
class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs): # must initialize
        super(MainWindow, self).__init__(*args, **kwargs) # always write this or won't work

        
        self.setWindowTitle('My Awesome App') #Set title
        
        
        #label
        label = QLabel("THIS IS AWESOME!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        #toolbar settings
        
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(20,20))
        self.addToolBar(toolbar)
        
        # first widget
        button_action = QAction(QIcon("bug.png"),"&Your button", self)
        button_action.setStatusTip("This is bug")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        toolbar.addSeparator()
        
        #second widget
        
        button_action2 = QAction(QIcon("car-red.png"),"Your &button2", self)
        button_action2.setStatusTip("This is car")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        toolbar.addSeparator()

        # third widget
        toolbar.addWidget(QLabel("Hello"))        
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu =  self.menuBar()
        menu.setNativeMenuBar(False) # Disables global menu bar on macos
        
        file_menu = menu.addMenu(u"&File")
        file_menu.addAction(button_action)
        
        file_menu.addSeparator()
        
        file_submenu = file_menu.addMenu("Submenu")
        
        file_submenu.addAction(button_action2)
        
    def onMyToolBarButtonClick(self, s):
        print("click",s)
        
        
#initialize app
app = QApplication(sys.argv)

# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default

# Run event loop

app.exec_()

