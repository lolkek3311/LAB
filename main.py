import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QVBoxLayout,QWidget
from rotating_wheel import RotatingWheel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LR 1')

        self.setGeometry(100,100,400,400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.wheel = RotatingWheel(self.central_widget)

        self.btn_move_right = QPushButton('Dvig v pravo')

        self.btn_move_right.clicked.connect(lambda:self.wheel.move(10,0))

        self.btn_rotate = QPushButton('Vrashat')

        self.btn_rotate.clicked.connect(lambda: self.wheel.rotate(15))

        self.layout.addWidget(self.wheel)
        self.layout.addWidget(self.btn_move_right)
        self.layout.addWidget(self.btn_rotate)

if __name__ =='__main__':
    app = QApplication(sys.argv)

    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
