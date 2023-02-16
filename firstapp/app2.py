"""
    App button will change app name and disable button when the name becomes
    a certain string from a list of strings
"""
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from random import choice

window_titles = [
    'App',
    'Cool App',
    'App Again',
    'Apples Cool',
    'Example Text',
    'Plaintext Title',
    'Catastrophic Disaster',
    'Explelliarmus Wingardium Leviosa'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.setFixedSize(QSize(400, 300))
        self.n_times_clicked=0

        self.button = QPushButton("Click! cLICK")

        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.window_title_change)
        self.button.setCheckable(True)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked")
        new_title = choice(window_titles)
        self.setWindowTitle(new_title)


    def window_title_change(self, window_title):
        if window_title == 'Apples Cool':
            self.button.setDisabled(True)

# sys.argv to allow cli arguments for app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec()
