from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
win_card = QWidget()
win_card.resize(600, 600)
win_card.move(350, 100)
win_card.setWindowTitle('Memory card')
win_menu = QPushButton('Меню')
win_rest = QPushButton('Відпочити')
win_next = QPushButton('Відповісти')
sp_rest = QSpinBox()
question = QLabel('Питаня')
minutes = QLabel('Питаня')
RadioGroupBox = QGroupBox()

RadioGroup = QButtonGroup()

rbton_ans1 = QRadioButton("1")
rbton_ans2 = QRadioButton("2")
rbton_ans3 = QRadioButton("3")
rbton_ans4 = QRadioButton("4")
RadioGroup.addButton(rbton_ans1)
RadioGroup.addButton(rbton_ans2)
RadioGroup.addButton(rbton_ans3)
RadioGroup.addButton(rbton_ans4)

layout_ans = QVBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()

layout_ans1.addWidget(rbton_ans1)
layout_ans1.addWidget(rbton_ans2)
layout_ans2.addWidget(rbton_ans3)
layout_ans2.addWidget(rbton_ans4)

layout_ans.addLayout(layout_ans1)
layout_ans.addLayout(layout_ans2)

RadioGroupBox.setLayout(layout_ans)


line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_1.addWidget(win_menu)
line_1.addStretch(1)
line_1.addWidget(win_rest)
line_1.addWidget(sp_rest)
line_1.addWidget(minutes)

line_2 = QHBoxLayout()
line_4 = QHBoxLayout()

main = QVBoxLayout()
main.addLayout(line_1)
main.addLayout(line_2)
main.addWidget(RadioGroupBox)
main.addLayout(line_4)
win_card.setLayout(main)
win_card.show()
app.exec_()