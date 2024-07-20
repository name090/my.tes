from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
button = QPushButton('згеренувати')
text = QLabel('натисни, ')
winner = QLabel('?')

v_line = QVBoxLayout()
v_line.addWidget(text, alignment = Qt.AlignCenter)
v_line.addWidget(button, alignment = Qt.AlignCenter)
v_line.addWidget(winner, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)



def show_winner():
    numder = randint(0,99)
    winner.setText(str(numder))

button.clicked.connect(show_winner)

main_win.show()
app.exec_()