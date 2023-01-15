import os
from PyQt5.QtCore import *
from openpyxl import Workbook

BASE_DIR = os.getcwd()

class ExcelWorker(QThread):
    def __init__(self):
        super().__init__()
        self.filter = ''

    def run(self):
        self.filter = 'tcp port 80'
        sniffing(self.filter, 0)

    def pause(self):
        self.filter = 'tcp port 80'
        sniffing(self.filter, 1)