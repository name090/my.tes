from memo_card_layout import *
from memo_data import Question
from random import *


qst1 = Question("Дім","huse","cet","dog","noice")
qst2 = Question("мишка","mouse","cet","pineardf","noice")
qst3 = Question("кіт","huse","cet","dog","noice")
pst4 = Question("пес","huse","dog","cet","noice")

list = [qst1,qst2,qst3]

# def randomQuestion():
#     global list
#     quesetion = choice(list)
#     radio_lict = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
#     shuffle(radio_lict)
#     answerRB = radio_lict[0]
#     wronge1 = radio_lict[1]
#     wronge2 = radio_lict[2]
#     wronge3 = radio_lict[3]
#     lb_Question.setText(quesetion.question)
#     rbtn_1.setText(quesetion.answer)
#     wronge1.setText(quesetion.wrong_answer1)
#     wronge2.setText(quesetion.wrong_answer2)
#     wronge3.setText(quesetion.wrong_answer3)

def clickok():
    show_result()


# randomQuestion()

btn_OK.clicked.connect(clickok)
app.exec_()