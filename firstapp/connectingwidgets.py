"""
    Practice in connecting widgets
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")


        # Set the objects
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        # Create a layout object and add the textline and label widget to it
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)


        # Create the widget object and set its layout to the 
        # layout object
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

# sys.argv to allow cli arguments for app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec()
