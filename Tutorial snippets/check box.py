# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:19:16 2017

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
        
       
        widget = QCheckBox()    
        widget.setCheckState(Qt.PartiallyChecked)
        widget.stateChanged.connect(self.show_state)
        
        
        self.setCentralWidget(widget)
        
    def show_state(self, s):
        print(s)
        
   
        
        
#initialize app
app = QApplication(sys.argv)

# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default

# Run event loop

app.exec_()

