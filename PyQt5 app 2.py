


# import * frowned upon but works in this case
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# import sys
import sys

# Class window
class MainWindow(QMainWindow):
    
    my_awesome_signal = pyqtSignal(str)
    def __init__(self, *args, **kwargs): # must initialize
        super(MainWindow, self).__init__(*args, **kwargs) # always write this or won't work

        
        self.setWindowTitle('My Awesome App') #Set title
        
        button = QPushButton("Hello fam!")
        button.pressed.connect(self.pushed_my_button)
        
        self.my_awesome_signal.connect(self.caught_my_own_signal)
        self.setCentralWidget(button)
        
    def contextMenuEvent(self, e):
        print("Context Menu requested!")
        super(MainWindow, self)
      
    def my_custom_fn(self, a): # custom funciton with default values
        print(a)

    def pushed_my_button(self):
        print("Pressed it!")
        self.my_awesome_signal.emit('WoAHH')
        
    def caught_my_own_signal(self, s):
        print(s)

#initialize app
app = QApplication(sys.argv)

# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default

# Run event loop

app.exec_()

