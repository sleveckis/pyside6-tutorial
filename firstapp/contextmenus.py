"""
    Practice for context menus (right click menus)

"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Signal-based approach
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))


# sys.argv to allow cli arguments for app
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec()
