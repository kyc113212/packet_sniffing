
from PyQt5.QtCore import *

class UiWorker(QThread):
    running_check = pyqtSignal(bool)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        # self.num = 0             # 초깃값 설정

        self.running = False

    def run(self):
        while self.running:
            self.running_check.emit(self.running)     # 방출
            #self.num += 1
            print("안녕하세요")
            self.sleep(1)

    def resume(self):
        self.running = True
        #Snapping

    def pause(self):
        self.running = False