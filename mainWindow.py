from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5 import QtTest
import time

def isDateValid(month, day):
    ret = True
    days = [31, 28, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31]

    if (month == '') or (month > 12) or (month < 1):
        ret = False
    elif (day == '') or (day > days[month - 1]) or (day < 1):
        ret = False
    return ret

def isMonthValid(month):
    ret = True

    return ret

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Airline View')
        self.layoutBase = QVBoxLayout()
        self.initInputField()
        self.initButton()
        self.initResultUI()
        self.show()
        self.setLayout(self.layoutBase)

    def initInputField(self):
        layout1 = QHBoxLayout()
        layout1.addStretch(1)

        self.monthInputField = QLineEdit(self, alignment=Qt.AlignRight)
        layout1.addWidget(self.monthInputField)
        self.monthLabel = QLabel('월')
        layout1.addWidget(self.monthLabel)

        self.dayInputField = QLineEdit(self, alignment=Qt.AlignRight)
        layout1.addWidget(self.dayInputField)
        self.dayLabel = QLabel('일')
        layout1.addWidget(self.dayLabel)

        layout2 = QHBoxLayout()
        self.initComboBox(layout2)

        self.layoutBase.addLayout(layout1)
        self.layoutBase.addLayout(layout2)

    def initComboBox(self, layout):
        companyLabel = QLabel("항공사")
        self.companyComboBox = QComboBox(self)
        self.companyComboBox.addItem("전부 표시")
        self.companyComboBox.addItem("대한항공")
        self.companyComboBox.addItem("아시아나항공")
        self.companyComboBox.addItem("에어부산")
        self.companyComboBox.addItem("제주항공")
        self.companyComboBox.addItem("진에어")
        self.companyComboBox.addItem("티웨이항공")

        sortUnitLabel = QLabel("정렬 기준")
        self.sortUnitLabelComboBox = QComboBox(self)
        self.sortUnitLabelComboBox.addItem("출발 시간순")
        self.sortUnitLabelComboBox.addItem("낮은 가격순")
        self.sortUnitLabelComboBox.addItem("높은 가격순")

        directionLabel = QLabel("방향")
        self.directionComboBox = QComboBox(self)
        self.directionComboBox.addItem("김포 -> 제주")
        self.directionComboBox.addItem("제주 -> 김포")

        layout.addWidget(companyLabel, alignment = Qt.AlignRight)
        layout.addWidget(self.companyComboBox, alignment = Qt.AlignRight)
        layout.addWidget(sortUnitLabel, alignment = Qt.AlignRight)
        layout.addWidget(self.sortUnitLabelComboBox, alignment = Qt.AlignRight)
        layout.addWidget(directionLabel, alignment = Qt.AlignRight)
        layout.addWidget(self.directionComboBox, alignment = Qt.AlignRight)

    def initButton(self):
        layout = QHBoxLayout()

        self.searchButton = QPushButton('찾기', self)
        layout.addWidget(self.searchButton, alignment = Qt.AlignRight)
        layout.setAlignment(Qt.AlignRight)
        self.searchButton.clicked.connect(self.onSearchButtonClicked)
        self.layoutBase.addLayout(layout)

    def initResultUI(self):
        resultTextLabel = QLabel("항공권: ", self)
        self.layoutBase.addWidget(resultTextLabel)

        self.resultTextEdit = QTextEdit(self)
        self.layoutBase.addWidget(self.resultTextEdit)

    def setSearchButtonCallback(self, callback):
        self.buttonCallback = callback

    def showAirline(self, airlineObj):
        size = airlineObj.getSize()
        text = ''
        if size == 0:
            text = '항공권이 존재하지 않습니다.'
        airlineOption = self.companyComboBox.currentText()
        for i in range(size):
            airlineName = airlineObj.getAirline(i)

            if airlineOption == airlineName or airlineOption == '전부 표시':
                text += airlineName + '\n'
                text += airlineObj.getAirlineStartTime(i) + ' 출발\n'
                text += airlineObj.getAirlineCost(i) + '원\n\n'

        self.resultTextEdit.setText(text)

    def onSearchButtonClicked(self):
        day = ''
        month = ''
        self.resultTextEdit.setText('항공권을 불러오는 중입니다...')
        QtTest.QTest.qWait(2)
        
        try:
            day = int(self.dayInputField.text())
            month = int(self.monthInputField.text())
        except ValueError:
            self.resultTextEdit.setText('Please Input an Int Value')

        if isDateValid(month, day):
            self.buttonCallback(day, month, self.directionComboBox.currentText(), self.sortUnitLabelComboBox.currentText())
        else:
            self.resultTextEdit.setText('올바른 날짜가 아닙니다.')
