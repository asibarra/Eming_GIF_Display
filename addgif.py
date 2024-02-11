from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        # Set the window to be fullscreen
        MainWindow.showFullScreen()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 480, 360))  # Match label size to window size
        self.label.setObjectName("label")

        # Embed the label into the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Load the GIF
        self.movie = QMovie("Eming_rotated.gif")
        self.label.setMovie(self.movie)

        # Scale the GIF to fit within the label and maintain aspect ratio
        self.movie.frameChanged.connect(self.scale_gif)
        self.movie.start()

    def keyPressEvent(self, event):
        # Handle the "Esc" key press to exit the application
        if event.key() == QtCore.Qt.Key_Escape:
            app.exit()

    def scale_gif(self):
        # Scale the GIF to fit within the label while maintaining aspect ratio
        frame = self.movie.currentPixmap()
        scaled_frame = frame.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(scaled_frame)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
