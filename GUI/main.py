import sys
from PyQt5 import QtWidgets
from gui import MainWindow
from control import ControlThread

class App(QtWidgets.QApplication):
    def __init__(self, args):
        super().__init__(args)
        
        self.main_window = MainWindow()
        self.control_thread = ControlThread(self.main_window.updateProgressBar)
        
        self.main_window.gripButton.clicked.connect(self.control_thread.gripOperation)
        self.main_window.dropButton.clicked.connect(self.control_thread.dropOperation)
        self.main_window.resetButton.clicked.connect(self.control_thread.resetOperation)
        
        self.main_window.show()
        self.control_thread.start()
    
if __name__ == "__main__":
    app = App(sys.argv)
    
    sys.exit(app.exec())