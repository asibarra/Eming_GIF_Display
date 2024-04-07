from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import RPi.GPIO as GPIO
import sys
import time
import os

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            self.is_playing = False
            self.is_sleeping = False

            # Set the window to be fullscreen
            MainWindow.showFullScreen()

            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")

            # Define a label for displaying GIF
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))  # Match label size to window size
            #self.label.setAlignment(QtCore.Qt.AlignCenter) # Center the label
            self.label.setObjectName("label")

            # Embed the label into the main window
            MainWindow.setCentralWidget(self.centralwidget)

            # Load the GIFS
            self.gifs= ["eye_closed.gif","Eming_wake.gif", "Eye_open.gif", "eye_squint.gif", "squint_still.gif"]
            self.movie_index = 0

            self.movie = QMovie(self.gifs[self.movie_index])
            self.label.setMovie(self.movie)

            self.movie.frameChanged.connect(self.scale_gif)
            self.movie.start()

            # Set up the GPIO for Pause Frame GIF Button
            GPIO.setmode(GPIO.BCM)
            self.pause_button = 14
            GPIO.setup(self.pause_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            # Set up the GPIO for Switch GIF button
            GPIO.setmode(GPIO.BCM)
            self.button_pin = 15
            GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            #Set up a QTimer for handing button presses
            self.button_timer = QtCore.QTimer(self.centralwidget)
            self.button_timer.timeout.connect(self.check_button_state)
            self.button_timer.start(200) # Check every 200 miliseconds
            self.setup_buttons


        def setup_buttons(self):
            GPIO.setmode(GPIO.BCM)
            self.wake_button = 23
            GPIO.setup(self.wake_button, GPIO.In, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(self.wake_button, GPIO.FALLING, callback=self.wake_pi, bouncetime=200)


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

        def toggle_play(self):
            self.is_playing = not self.is_playing
            if self.is_playing:
                print("Play")
                self.movie.start()
            else:
                print("Pause")
                self.movie.stop()

        def check_button_state(self):
            # Check if the button is pressed and change the GIF accordingly
            if GPIO.input(self.button_pin) == GPIO.LOW:
                self.change_gif()

            # Check if play/pause button is pressed. Play/pause logic on toggle
            if GPIO.input(self.pause_button) == GPIO.LOW:
               self.toggle_play()
               time.sleep(0.2)
               while GPIO.input(self.button_pin) == GPIO.LOW:
                   pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    GPIO.setmode(GPIO.BCM)

    try:
        sys.exit(app.exec_())

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        GPIO.cleanup()

