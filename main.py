from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '5259101785:AAHNsgI-yc-NDB8pElbgl8uroQM6wQiWIBU'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

from Keyboard import *


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, хочешь поиграть?", reply_markup=Kb)

@dp.message_handler(text='Нет')
async def process_start_command(message: types.Message):
    await message.reply("Ну и ладно.")

@dp.message_handler(text='Да')
async def process_start_command(message: types.Message):
    await message.reply("Ты проснулся ночью в лесу не помня как тут очутился. \n"
                        "Tебе холодно и ты начал искать по корманам что есть чтобы согреться. \n"
                        "И тут ты находишь: \n"
                        "1) Зажигалку \n"
                        "2)Фонарик \n"
                        "3)ключи \n"
                        "Выбери то что тебе поможет согреться.",reply_markup=Kb2)

@dp.message_handler(text='Фонарик')
async def process_start_command(message: types.Message):
    await message.reply("Ну в будущем может и пригодится, но не сейчас)",reply_markup=Kb2)

@dp.message_handler(text='Ключи')
async def process_start_command(message: types.Message):
    await message.reply("ЗАЧЕМ ОНИ ТЕБЕ?",reply_markup=Kb2)

@dp.message_handler(text='Зажигалка')
async def process_start_command(message: types.Message):
    await message.reply("Молодец, ты только что разжёг костёр. Ты согрелся и полон сил. \n"
                        "Но вдруг в тепле у тебя проснулся аппетит, но кушать нечего, кроме таракана которого ты только, заметил.",reply_markup=Kb3)


@dp.message_handler(text='Скушать таракана')
async def process_start_command(message: types.Message):
    await message.reply("Ну где мозги надо иметь а?\nТЫ УМЕР И ПРОИГРАЛ!\n"
                        "Желаешь сыграть ещё раз?", reply_markup=Kb)


@dp.message_handler(text='Встать с тёплого места и пойти искать хоть что-то чтоб выжить здесь')
async def process_start_command(message: types.Message):
    await message.reply("Ты шёл пол часа и вдруг в далеке замечаешь кемперский лагерь в котором не горит свет. \n"
                        "Ты начинаешь всё быстрее и быстрее идти к нему, но услышав страшный звук справа начинаешь бежать. Пока бежишь ты оглядываешься и не кого не видишь, но вдруг уже подбегая к лагерю ты спотыкаешься об корень дерева торчащий из земли и падаешь.\n"
                        "Ты поднимаешься и чувствуя боль в ноге осматриваешь себя. При падении ты раскровил себе колено.\n"
                        "Храмая, еле как ты всё таки доходишь до своей цели и понимая, что тут недавно были люди, но они куда то ушли, думаешь что тебе делать.", reply_markup=Kb4)

@dp.message_handler(text='Да нафиг этот лагерь, лучше пойду ещё поброжу')
async def process_start_command(message: types.Message):
    await message.reply("Ты пошёл дальше бродить, но чувствуя голод и недомогание(от потери крови), заснул и уснул вечныйм сном.\n"
                        "Ты проиграл\n"
                        "Желаешь сыграть ещё раз?", reply_markup=Kb)

@dp.message_handler(text='Быстрее найти еду, а то жрать то хочется)')
async def process_start_command(message: types.Message):
    await message.reply("Ты нашёл еду и славно похавал бутеров.",reply_markup=Kb5)

@dp.message_handler(text='Поискать какие либо медикаменты, чтоб остановить кровь.')
async def process_start_command(message: types.Message):
    await message.reply("Ты нашёл аптечку, обеззаразил спиртом ногу и замотал бинтом.",reply_markup=Kb6)

@dp.message_handler(text='Ну теперь и медикаменты можно поискать')
async def process_start_command(message: types.Message):
    await message.reply("Ты нашёл аптечку, обеззаразил спиртом ногу и замотал бинтом.\n"
                        "Ты почувствовал сильную усталость и решил передохнуть лёжа в полатке, но вдруг неожиданно уснул.", reply_markup=Kb7)

@dp.message_handler(text='Ну теперь можно и еду поискать')
async def process_start_command(message: types.Message):
    await message.reply("Ты нашёл еду и славно похавал бутеров.\n"
                        "Ты почувствовал сильную усталость и решил передохнуть лёжа в полатке, но вдруг неожиданно уснул.", reply_markup=Kb7)

@dp.message_handler(text='Проснуться')
async def process_start_command(message: types.Message):
    await message.reply("Ты просыпаешься, от шагов рядом с палаткой, не понимая чьи они.\n"
                        "Тебе страшно.\n"
                        "Ты лежишь притоивший и в голове у тебя всего 2 идеи.",reply_markup=Kb8)

@dp.message_handler(text='Выскачить и тоже напугат то, что находить вне палатки, а то внатуре чё оно меня пугает.')
async def process_start_command(message: types.Message):
    await message.reply("Ты резко выскакиваешь из палатки, включаешь фонарик и бежишь на звуки шагов оря как дикий.\n"
                        "Оказывается это был человек,и от неожиданности стреляет в тебя из охотнечего ружья\n"
                        "Ты проиграл!\n"
                        "Желаешь сыграть ещё раз", reply_markup=Kb)

@dp.message_handler(text='Лежать дальше не издавая ни звука.')
async def process_start_command(message: types.Message):
    await message.reply("Палатка откравается и издаётся крик.\n"
                        "Это люди. Они начинают выеснять у тебя кто ты и что забыл в палатке.",reply_markup= Kb9)

@dp.message_handler(text='Молчать до последнего.')
async def process_start_command(message: types.Message):
    await message.reply("Они начинают психовать и выходить из себя.\n"
                        "Терпение лопается и они выгоняют тебя из лагеря.\n"
                        "И вот ты снова один. Блуждая по лесу на тебя кападает волк и ты умераешь.\n"
                        "ТЫ ПРОИГРАЛ!\n"
                        "Желаешь сыграть ещё раз?", reply_markup=Kb)

@dp.message_handler(text='Рассказать им всё о том что ты знаешь, вдруг помогут.')
async def process_start_command(message: types.Message):
    await message.reply("Ты им рассказываешь свой путь в деталях и то что не помнишь как тут очутился.\n"
                        "Прослушав твою историю они решили помочь тебе и на следующий день пойти в сторону дороги к их машине, чтоб увезти тебя отсюда.\n"
                        "Вы начинаете разговор и ты узнаешь много о них. Например то, что они охотники и каждые выходние ездядт в этот лес за добычей. Они разрешили тебе поспать в палатке человека который ночью будет стоять на стороже.\n"
                        "Чувствуя усталость ты идёшь спать.\n"
                        "На утро вы с новыми силами, бодрые решаете пойти к машине, не смотря на дождь.\n"
                        "Проходит 30 минут и вы уже стоите у машины. Не долго думая вы садитесь и едете в сторону города.\n"
                        "Ты радостный едешь думая, что скоро будешь дома\n"
                        "Но тут машина уходит в занос и вы улетаете в канаву.\n"
                        "Ты теряешь сознание.", reply_markup= Kb10)

@dp.message_handler(text='Проснуться!')
async def process_start_command(message: types.Message):
    await message.reply("Ты проснулся ночью в лесу не помня как тут очутился. \n"
                        "Tебе холодно и ты начал искать по корманам что есть чтобы согреться. \n"
                        "И тут ты находишь: \n"
                        "1) Зажигалку \n"
                        "2)Фонарик \n"
                        "3)ключи \n"
                        "Выбери то что тебе поможет согреться.",reply_markup=Kb2)


if __name__ == '__main__':
    executor.start_polling(dp)