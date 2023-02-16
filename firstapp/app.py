
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        #self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(300, 250))
        self.setMaximumSize(QSize(500, 400))

        button = QPushButton("Click! cLICK")
        self.button_state = True
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.button_toggle)
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked")

    def button_toggle(self, checkedstate):
        self.button_state = checkedstate
        print("Checked?", self.button_state)

# sys.argv to allow cli arguments for app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec()
