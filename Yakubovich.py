from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()
text = QLabel("в якому році він отримав золоту кнопку")
vidpovid1 = QRadioButton("2005")
vidpovid2 = QRadioButton("2010")
vidpovid3 = QRadioButton("2015")
vidpovid4 = QRadioButton("2020")

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(text, alignment = Qt.AlignCenter)
line2.addWidget(vidpovid1, alignment = Qt.AlignCenter)
line2.addWidget(vidpovid2, alignment = Qt.AlignCenter)
line3.addWidget(vidpovid3, alignment = Qt.AlignCenter)
line3.addWidget(vidpovid4, alignment = Qt.AlignCenter)


line = QVBoxLayout()
line.addLayout(line1)
line.addLayout(line2)
line.addLayout(line3)





# v_line.addWidget(text, alignment = Qt.AlignCenter)
# v_line.addWidget(vidpovid1, alignment = Qt.AlignCenter)
# v_line.addWidget(vidpovid2, alignment = Qt.AlignCenter)
# v_line.addWidget(vidpovid3, alignment = Qt.AlignCenter)
# v_line.addWidget(vidpovid4, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def correct():
    victory_win = QMessageBox()
    victory_win.setText("Прпвильно")
    victory_win.exec_()

def fail():
    victory_win = QMessageBox()
    victory_win.setText("не Прпвильно")
    victory_win.exec_()
    
vidpovid1.clicked.connect(correct)
vidpovid2.clicked.connect(fail)
vidpovid3.clicked.connect(fail)
vidpovid4.clicked.connect(fail)
main_win.show()
app.exec_()