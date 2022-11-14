from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton('Да')
button2 = KeyboardButton('Нет')

Kb = ReplyKeyboardMarkup()
Kb.add(button1)
Kb.add(button2)

button3 = KeyboardButton('Зажигалка')
button4 = KeyboardButton('Фонарик')
button5 = KeyboardButton('Ключи')

Kb2 = ReplyKeyboardMarkup()
Kb2.add(button3)
Kb2.add(button4)
Kb2.add(button5)

button6 = KeyboardButton('Встать с тёплого места и пойти искать хоть что-то чтоб выжить здесь')
button7 = KeyboardButton('Скушать таракана')


Kb3 = ReplyKeyboardMarkup()
Kb3.add(button6)
Kb3.add(button7)

button8 = KeyboardButton('Быстрее найти еду, а то жрать то хочется)')
button9 = KeyboardButton('Поискать какие либо медикаменты, чтоб остановить кровь.')
button10 = KeyboardButton('Да нафиг этот лагерь, лучше пойду ещё поброжу')

Kb4 = ReplyKeyboardMarkup()
Kb4.add(button8)
Kb4.add(button9)
Kb4.add(button10)

button11 = KeyboardButton('Ну теперь и медикаменты можно поискать')

Kb5 = ReplyKeyboardMarkup()
Kb5.add(button11)

button12 = KeyboardButton('Ну теперь можно и еду поискать')

Kb6 = ReplyKeyboardMarkup()
Kb6.add(button12)

button13 = KeyboardButton('Проснуться')

Kb7 = ReplyKeyboardMarkup()
Kb7.add(button13)

button14 = KeyboardButton('Выскачить и тоже напугат то, что находить вне палатки, а то внатуре чё оно меня пугает.')
button15 = KeyboardButton('Лежать дальше не издавая ни звука.')

Kb8 = ReplyKeyboardMarkup()
Kb8.add(button14)
Kb8.add(button15)

button16 = KeyboardButton('Молчать до последнего.')
button17 = KeyboardButton('Рассказать им всё о том что ты знаешь, вдруг помогут.')

Kb9 = ReplyKeyboardMarkup()
Kb9.add(button16)
Kb9.add(button17)

button18 = KeyboardButton('Проснуться!')

Kb10 = ReplyKeyboardMarkup(resize_keyboard=True)
Kb10.add(button18)

