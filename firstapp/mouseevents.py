"""
    Example of mouse events and overriding normal handler events
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label=QLabel("Click in here")
        self.setCentralWidget(self.label)

    """
        Overriding the behavior of each handler event by printing the event's name to
        the label. e will receive the incoming event, we can identify which it is specifically,
        and modify behavior accordingly. For brevity I'll only do this on mousePressEvent
    """
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

        if e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")



# sys.argv to allow cli arguments for app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec()
