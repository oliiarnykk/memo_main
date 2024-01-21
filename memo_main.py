
#підключення бібліотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QMessageBox,QRadioButton
from random import randint
app=QApplication([])
# Зберігання посилання на вікно "Транспорт"
transport_win = None
#створення дод вікон
def show_paris():
    victory_win=QMessageBox()
    victory_win.setText('Бразилія - це найбільша країна Південної Америки, яка славиться своєю різноманітною культурою, природною красою та веселою атмосферою. Ріо-де-Жанейро - одне з найвідоміших міст, з відомим пляжем Копакабана та статуєю Христа-Спасителя. Амазонка - найбільший тропічний ліс у світі, є природною родзинкою Бразилії. Країна також відома своєю пестливою відносиною до футболу, оскільки це місце народження багатьох видатних футболістів та місце проведення Всесвітнього кубка з футболу у 2014 році. ''')
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_london():
    victory_win=QMessageBox()
    victory_win.setText('''
Німеччина - це розташована в центрі Європи країна з багатим культурним спадком. Тут ви знайдете чудові міста, такі як Берлін, Мюнхен, Кельн та Гамбург, зі знаменитими архітектурними пам'ятками, музеями та ресторанами. Країна славиться своєю традиційною кухнею, зокрема ковбасами та пивом.''')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_german():
    victory_win=QMessageBox()
    victory_win.setText('''Португалія - захоплююча країна на південному заході Європи з багатою історією та чарівними пейзажами. Лісабон, столиця, приваблює своєю колоритною архітектурою, вуличними музикантами та виглядами на річку Тежу. У Португалії багато прекрасних пляжів на узбережжі Атлантичного океану, зокрема на Алгарве. Країна відома своєю традиційною кухнею, де головні страви - це морепродукти та пастишші.''')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_itali():
    victory_win=QMessageBox()
    victory_win.setText('Японія - країна у Східній Азії, яка поєднує сучасні технології з глибокими традиціями. Токіо, столиця, є мегаполісом з вражаючими хмарочосами, магазинами та ресторанами. Країна славиться своєю високотехнологічною індустрією, інноваціями та науковими досягненнями. Японія також відома своєю унікальною культурою, включаючи чаюну церемонію, кімоно та гейш. Країна багата на історичні та релігійні споруди, такі як храми та святині.')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_amer():
    victory_win=QMessageBox()
    victory_win.setText('Іспанія - країна, розташована на Піренейському півострові, відома своєю багатою історією, культурою та красивими пляжами. Мадрид, столиця, має величезні музеї, архітектурні шедеври та пульсуюче міське життя. Барселона славиться архітектурними творіннями Антоні Гауді, включаючи Саграда Фамілію. Іспанія відома також своєю традиційною кухнею, з паельєю, тапасами та смачними винами.')
    victory_win.setStyleSheet("font-size: 16px; font-weight: bold;")
    victory_win.setWindowTitle('Країна')
    victory_win.exec_()
def show_litak():
    victory_win=QMessageBox()
    victory_win.setText('Вірно ти виграв!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_korabel():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_poizd():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
def show_car():
    victory_win=QMessageBox()
    victory_win.setText('Ні 2015 ти мав вибрати!')
    victory_win.setWindowTitle('Час та кошти')
    victory_win.exec_()
#Створення другого вікна (2 вікно)   
def show_trans():
    global transport_win
    transport_win = QWidget()
    transport_win.setWindowTitle('Транспорт')
    transport_win.resize(530, 530)
    transport_win.setStyleSheet("background-color: 	#FFB6C1; font-size: 16px; font-weight: bold;")

    question = QLabel('На чому ви хочете їхати?')
    btn_transport1 = QRadioButton('Літак')
    btn_transport2 = QRadioButton('Поїзд')
    btn_transport3 = QRadioButton('Автомобіль')
    btn_transport4 = QRadioButton('Корабель')

    btn_styles = "font-size: 16px; font-weight: bold;"
    btn_transport1.setStyleSheet(btn_styles)
    btn_transport2.setStyleSheet(btn_styles)
    btn_transport3.setStyleSheet(btn_styles)
    btn_transport4.setStyleSheet(btn_styles)

    layout_main = QVBoxLayout()
    layoutH1 = QHBoxLayout()
    layoutH2 = QHBoxLayout()

    layoutH1.addWidget(question, alignment=Qt.AlignCenter)
    layoutH2.addWidget(btn_transport1, alignment=Qt.AlignCenter)
    layoutH2.addWidget(btn_transport2, alignment=Qt.AlignCenter)
    layoutH2.addWidget(btn_transport3, alignment=Qt.AlignCenter)
    layoutH2.addWidget(btn_transport4, alignment=Qt.AlignCenter)

    layout_main.addLayout(layoutH1)
    layout_main.addLayout(layoutH2)

    transport_win.setLayout(layout_main)

    btn_transport1.clicked.connect(show_litak)
    btn_transport2.clicked.connect(show_poizd)
    btn_transport3.clicked.connect(show_car)
    btn_transport4.clicked.connect(show_korabel)
    transport_win.show()
#Створення головного (1вікна)
main_win=QWidget()
main_win.setWindowTitle('Подорожі')
main_win.resize(530,530)
#Колір фону та розмір тексту
main_win.setStyleSheet("background-color: 	#FFA07A; font-size: 16px; font-weight: bold;")
#створення віджетів головного вікна
question=QLabel('В яку країну ви хочете поїхати?')
btn_answer1=QRadioButton('Німеччина')
btn_answer2=QRadioButton('Бразилія')
btn_answer3=QRadioButton('Португалія')
btn_answer4=QRadioButton('Японія')
btn_answer5=QRadioButton('Іспанія')
btn_next=QPushButton('На чому їдемо?')#Кнопка по середині
# Застосування стилів до кнопок(шрифт)
text_styles = "font-size: 16px; font-weight: bold;"
btn_answer1.setStyleSheet(text_styles)
btn_answer2.setStyleSheet(text_styles)
btn_answer3.setStyleSheet(text_styles)
btn_answer4.setStyleSheet(text_styles)
btn_answer5.setStyleSheet(text_styles)
btn_next.setStyleSheet("font-size: 16px; font-weight: bold; background-color: #c1ccde;")
#розташування віджетів по лейаутам
layout_main= QVBoxLayout()
layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()
layoutH4=QHBoxLayout()

layoutH1.addWidget(question,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1,alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2,alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_next,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer3,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer4,alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer5,alignment=Qt.AlignCenter)


layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
main_win.setLayout(layout_main)
#обробка натискань на перемикачі
btn_answer1.clicked.connect(show_london)
btn_answer2.clicked.connect(show_paris)
btn_answer3.clicked.connect(show_german)
btn_answer4.clicked.connect(show_itali)
btn_answer5.clicked.connect(show_amer)
btn_next.clicked.connect(show_trans)


#відображення вікна додатка 
main_win.show()
app.exec_()
