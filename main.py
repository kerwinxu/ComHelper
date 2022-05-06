from MainWindow import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication
import sys
from PySide2.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    '''这个是主窗口'''
    def __init__(self) -> None:
        super().__init__()
        # 这里调用的是窗口的ui界面
        # self.ui = QUiLoader().load('MainWindow.ui') # 用这个好像不能自动补全。
        # 我用一个脚本来将ui文件转成py文件，然后用如下的方式来初始化。
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__  == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow.ui.show()
    mainWindow.show()
    app.exec_()