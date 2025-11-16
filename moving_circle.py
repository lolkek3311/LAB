from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter,QColor,QPen
from PyQt5.QtCore import QRect

class MovingCircle(QWidget):
    def __init__ (self, parent=None, x=50,y=50,radius = 30):
        super().__init__(parent)
        self.x = x
        self.y = y
        self.radius = radius

        self.color = QColor(0,0,255)



    def move(self,dx,dy):
        self.x +=dx
        self.y +=dy

        self.update()

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor(0,0,0),2))

        painter.setBrush(self.color)
        painter.drawEllipse(self.x,self.y,self.radius*2,self.radius * 2)