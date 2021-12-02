from GMPtoCJU import GMPtoCJU
from CJUtoGMP import CJUtoGMP
from mainWindow import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime

def onSearchButtonClicked(day, month, direction, sortUnit):
    airlineObject = ''

    curDate = datetime.today()
    year = curDate.year
    if curDate.month > month or (curDate.month == month and curDate.day > day):
        year += 1
    month = format(month, '02')
    day = format(day, '02')
    
    if direction == '김포 -> 제주':
        airlineObject = GMPtoCJU(year, month, day)
    else:
        airlineObject = CJUtoGMP(year, month, day)

    if sortUnit == '출발 시간순':
        airlineObject.sortStartTime()
    elif sortUnit == '낮은 가격순':
        airlineObject.sortMoneyLowToHigh()
    else:
        airlineObject.sortMoneyHightToLow()

    mainWindow.showAirline(airlineObject)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setSearchButtonCallback(onSearchButtonClicked)
    sys.exit(app.exec_())
