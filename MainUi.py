from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from SnippingWorker import SnippingWorker
from UiWorker import UiWorker


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.uiWorker = UiWorker()
        self.uiWorker.start()
        self.uiWorker.running_check.connect(self.running_check)   # 시그널 슬롯 등록

        self.snippingWorker = SnippingWorker()

    def init_ui(self):
        self.setGeometry(500, 500, 400, 300)
        # self.edit = QLineEdit(self)
        # self.edit.move(10, 10)

        self.label = QLabel("시작 전 입니다", self)
        self.label.move(10, 50)
        self.label.setAlignment(Qt.AlignCenter)
        font1 = self.label.font()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.adjustSize()

        resumeBtn = QPushButton("resume", self)
        resumeBtn.move(10, 100)
        pauseBtn = QPushButton("pause", self)
        pauseBtn.move(10, 150)
        saveBtn = QPushButton("save", self)
        saveBtn.move(10, 200)

        # 시그널-슬롯 연결하기
        resumeBtn.clicked.connect(self.resume)
        pauseBtn.clicked.connect(self.pause)
        saveBtn.clicked.connect(self.save)

    @pyqtSlot(bool)
    def running_check(self, running):
        if running:
            self.label.setText('동작 중 입니다')
        else:
            self.label.setText('정지 중 입니다')

    def resume(self):
        self.uiWorker.resume()
        self.uiWorker.start()
        self.snippingWorker.start()

    def pause(self):
        self.uiWorker.pause()
        self.snippingWorker.pause()
        self.label.setText('정지 중 입니다')

    def save(self):
        self.label.setText('저장 합니다')