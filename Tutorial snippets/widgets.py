# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:42:45 2017

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
        
        
               
        layout = QVBoxLayout()
        
        
        widgets = [QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial,
                  QDoubleSpinBox, QFontComboBox, QLCDNumber, QLabel, QLineEdit,
                  QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox,
                  QTimeEdit]
        
        for w in widgets:
            layout.addWidget(w())
                
        widget = QWidget()    
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
        
   
        
        
#initialize app
app = QApplication(sys.argv)

# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default

# Run event loop

app.exec_()

