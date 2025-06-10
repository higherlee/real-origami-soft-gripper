from PyQt5 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Gripper Controller')
        self.resize(300, 300)
        
        self.progressBar = QtWidgets.QProgressBar()
        self.gripButton  = QtWidgets.QPushButton('Grip')
        self.dropButton  = QtWidgets.QPushButton('Drop')
        self.resetButton = QtWidgets.QPushButton('Reset')
        
        self.statusLabel = QtWidgets.QLabel("Waiting...")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)


        central_widget  = QtWidgets.QWidget()
        layout          = QtWidgets.QVBoxLayout(central_widget)
        hbox            = QtWidgets.QHBoxLayout()
        
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.progressBar)
        layout.addLayout(hbox)

        hbox.addWidget(self.gripButton)
        hbox.addWidget(self.dropButton)
        hbox.addWidget(self.resetButton)
        
        self.setCentralWidget(central_widget)

        
    def updateProgressBar(self, value, status):
        self.progressBar.setValue(value)
        self.statusLabel.setText(status)