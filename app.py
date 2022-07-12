 # ----------------------------------------------------------------------- #
#                                  config.py                                #
# ------------------------------------------------------------------------- #
#                           Copyright (c) 2022 SFXDevel                     #
#                           ______     ______   __  __                      #
#                          /\  ___\   /\  ___\ /\_\_\_\                     #
#                          \ \___  \  \ \  __\ \/_/\_\/_                    #
#                           \/\_____\  \ \_\     /\_\/\_\                   #
#                            \/_____/   \/_/     \/_/\/_/                   #
#                            https://github.com/SFXDevel                    #
 # ----------------------------------------------------------------------- #
# Permission is hereby granted, free of charge, to any person obtaining     #
# a copy of this software and associated documentation files (the           #
# "Software"), to deal in the Software without restriction, including       #
# without limitation the rights to use, copy, modify, merge, publish,       #
# distribute, sublicense, and#or sell copies of the Software, and to        #
# permit persons to whom the Software is furnished to do so, subject to     #
# the following conditions:                                                 #
#                                                                           #
# The above copyright notice and this permission notice shall be            #
# included in all copies or substantial portions of the Software.           #
#                                                                           #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,           #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF        #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.   #
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY      #
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,      #
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE         #
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                    #
 # ----------------------------------------------------------------------- #

from PyQt5.QtWidgets import QLabel 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import sys

global screenX
global screenY

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        app = QApplication.instance()
        screenObj = app.primaryScreen().availableGeometry()
        screenX = screenObj.width()
        screenY = screenObj.height()
        self.setAutoFillBackground(True)
        #colorPalette = self.palette()
        #colorPalette.setColor(self.backgroundRole(), Qt.red)
        #self.setPalette(colorPalette)
        self.setGeometry(screenX / 10 , screenY / 5 , screenX * 0.8, screenY * 0.7)
        self.setWindowTitle("VOID ~ Welcome")
        

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    welcomeWindow = WelcomeWindow()
    welcomeWindow.show()
    sys.exit(Application.exec_())