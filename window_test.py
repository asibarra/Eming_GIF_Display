from PyQt5 import QtWidgets, QtGui, QtCore

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 360))

        self.movie = QtGui.QMovie("Eming_Squint.gif")
        self.label.setMovie(self.movie)

        self.movie.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()