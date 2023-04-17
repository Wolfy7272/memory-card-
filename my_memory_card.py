from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q): #что то
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question1)
    show_question()

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 200)
button = QPushButton('Ответить')
question = QLabel()

def show_result(): #обработка нажатия на кнопку с надписью "ответить"
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Следующий вопрос")

def show_question(): #обработка нажатия на кнопку с надписью "следующий вопрос"
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText("Ответить")
    group_button = QButtonGroup()
    group_button.addButton(cat1)
    group_button.addButton(cat2)
    group_button.addButton(cat3)
    group_button.addButton(cat4)
    group_button.setExclusive(False)
    cat1.setChecked(False)
    cat2.setChecked(False)
    cat3.setChecked(False)
    cat4.setChecked(False)
    group_button.setExclusive(True)

def check_answer(q): #проверка правильности ответа
    if answer[0].isChecked():
        lb_Correct.setText(q.right_answer)
        show_correct("Правильно")
        window.score += 1

    if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        lb_Correct.setText(q.right_answer)
        show_correct("Неверно")

def show_correct(res): #установка текста результата и отображение формы ответа
    lb_Result.setText(res)
    show_result()

window.cur_question = -1

def next_question(): #следующий вопрос
    window.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]

    ask(q)

def click_ok():
    if button.text() == "Ответить":
        check_answer(question_list[0])

    if button.text() == "Следующий вопрос":
        next_question()

RadioGroupBox = QGroupBox("Варианты ответов")
cat1 = QRadioButton()
cat2 = QRadioButton()
cat3 = QRadioButton()
cat4 = QRadioButton()

answer = [cat1, cat2, cat3, cat4]

layout1 = QHBoxLayout()   
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout_card = QVBoxLayout()

layout2.addWidget(cat1) 
layout2.addWidget(cat2)

layout3.addWidget(cat3) 
layout3.addWidget(cat4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioGroupBox.setLayout(layout1)

layout_card.addWidget(question, alignment = Qt.AlignCenter)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('верно/неверно') 
lb_Correct = QLabel('ответ') 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)  
layout_card.addWidget(AnsGroupBox)

AnsGroupBox.hide() 

layout3.addStretch(1)
layout3.addWidget(button, stretch=2) 
layout3.addStretch(1)

layout_card.setSpacing(5) 

layout_card.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layout_card.addWidget(button, alignment = Qt.AlignCenter)

window.setLayout(layout_card)

question_list = []

question_list.append(Question("Как называется столица Польши?", "Варшава", "Рига", "Берлин", "Париж"))
question_list.append(Question("Как называется столица Швейцарии?", "Берн", "Москва", "Стокгольм", "Вильнюс"))
question_list.append(Question("Как называется столица Испании?", "Барселона", "Таллин", "Токио", "Пекин"))

window.total = 0
window.score = 0
next_question()
button.clicked.connect(click_ok)

window.show() 
app.exec()