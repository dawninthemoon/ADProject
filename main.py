from GMPtoCJU import GMPtoCJU
from CJUtoGMP import CJUtoGMP
from mainWindow import MainWindow
import sys
from PyQt5.QtWidgets import QApplication

def onSearchButtonClicked(day, month, direction, sortUnit):
    airlineObject = ''
    if direction == '김포 -> 제주':
        airlineObject = GMPtoCJU(month, day)
    else:
        airlineObject = CJUtoGMP(month, day)

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