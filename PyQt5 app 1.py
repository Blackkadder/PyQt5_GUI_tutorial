
# coding: utf-8

# In[1]:


# import * frowned upon but works in this case
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# import sys
import sys


# In[7]:


# Class window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs): # must initialize
        super(MainWindow, self).__init__(*args, **kwargs) # always write this or won't work

        self.setWindowTitle('My Awesome App') #Set title

        label = Qlabel('Praise Rhllor') #label text
        label.setAlignment(Qt.AlignCenter) #align center

        self.setCentralWidget(label) #set window n center


# In[8]:


#initialize app
app = QApplication(sys.argv)


# In[ ]:


# Create a window instance and show window
window = MainWindow()
window.show() # important. Windows are invisible by default


# In[ ]:


# Run event loop

app.exec_()


# In[ ]:





# In[ ]:
