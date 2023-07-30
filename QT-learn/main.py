from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton


def first():
    app = QApplication([])
    windows = QMainWindow()
    windows.resize(500, 400)
    windows.move(300, 300)
    windows.setWindowTitle("开始文本")

    textEdit = QPlainTextEdit(windows)
    textEdit.setPlaceholderText("please input salary")
    textEdit.move(10, 25)
    textEdit.resize(300, 500)

    button = QPushButton("统计", windows)
    button.move(380, 80)
    button.clicked.connect(handleCalc)
    windows.show()
    app.exec()


def handleCalc():
    """槽函数"""

    print("This button click")


if __name__ == '__main__':
    first()
