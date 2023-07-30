from PyQt5.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Stats:
    def __init__(self):
        qfile_stats = QFile("ui/ces.ui")
        qfile_stats.open(QFile.readyRead)
        qfile_stats.close()
        self.ui = QUiLoader().load(qfile_stats)
        self.ui.button.clicked.connect(self.handle)
