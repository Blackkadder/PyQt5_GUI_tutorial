


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
        
       
        #widget = QComboBox()    
    
        widget = QListWidget()            #also ise QListWidget
        widget.addItems(["One","Two","Three"])
        #widget.currentIndexChanged.connect(self.index_changed) #combo box
        widget.currentItemChanged.connect(self.index_changed) #list box
        
        widget.currentTextChanged[str].connect(self.text_changed)
        
        self.setCentralWidget(widget)
        
    def index_changed(self, s):
        print(s)
        
    def text_changed(self, s):
        print(s)        
   
        
        
#initialize app
app = QApplication(sys.argv)

# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default

# Run event loop

app.exec_()

