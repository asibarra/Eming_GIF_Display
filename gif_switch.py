from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import RPi.GPIO as GPIO
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

            # Load the GIFS
            self.gifs= ["Eming_rotated.gif", "Eming_Squint.gif"]
            self.movie_index = 0

            self.movie = QMovie(self.gifs[self.movie_index])
            self.label.setMovie(self.movie)

            self.movie.frameChanged.connect(self.scale_gif)
            self.movie.start()

            # Set up the GPIO for button
            GPIO.setmode(GPIO.BCM)
            self.button_pin = 15
            GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            #Set up a QTimer for handing button presses
            self.button_timer = QtCore.QTimer(self.centralwidget)
            self.button_timer.timeout.connect(self.check_button_state)
            self.button_timer.start(200) # Check every 200 miliseconds

        def keypressevent(self, event):
            # Handle the "Esc" key press to exit the application
            if event.key() == QtCore.Qt.Key_Escape:
                app.exit()

        def scale_gif(self):
            # Scale the GIF to fit within the lael while maintaining the aspect ratio
            frame = self.movie.currentPixmap()
            scaled_frame = frame.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(scaled_frame)

        def change_gif(self):
            # Stop the current QMovie before changing to the next one
            self.movie.stop()

            # Change the gif to the next one in the list
            self.movie_index = (self.movie_index + 1) % len(self.gifs)
            self.movie.setFileName(self.gifs[self.movie_index])
            self.movie.start()

        def check_button_state(self):
            # Check if the button is pressed and change the GIF accordingly
            if GPIO.input(self.button_pin) == GPIO.LOW:
                self.change_gif()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    try:
        sys.exit(app.exec_())
    
    except KeyboardInterrupt:
        print("Exiting...")
    
    finally:
        GPIO.cleanup()
