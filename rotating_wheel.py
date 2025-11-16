from moving_circle import MovingCircle
from PyQt5.QtGui import QPainter, QColor, QPen

class RotatingWheel(MovingCircle):
    def __init__(self,parent=None, x = 50 , y = 50 , radius = 40):
        super().__init__(parent,x,y,radius)

        self.angle = 0
        self.color = QColor(255,0,0)

    def rotate(self,angle_delta):
        self.angle = (self.angle+angle_delta)% 360

        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
 
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(QColor(0,0,0),2))


        painter.save()


        painter.translate(self.x+self.radius,self.y+self.radius)


        painter.rotate(self.angle)

        for i in range(4):
            painter.drawLine(0, -self.radius, 0, self.radius)

            painter.rotate(45)


        painter.restore()