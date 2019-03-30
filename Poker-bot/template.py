"""
Это шаблон кода телеграм бота.
Вы можете использовать его как основу для своих ботов.
"""

#
# Подключение библиотек
#

import os
from random import randint
import yaml
from Combo_model import combo
from collections import namedtuple
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler

#
# Общие константы
#

BOT_ID = "@PokerFatherbot"
BOT_TOKEN = "776645026:AAFUCgXTBaKdLHJRmrB6q-gOSWe1bAlsGQY"
BOT_APPNAME = "poker-bott"

#
# Тип данных
#

User = namedtuple("User", (
    "id",
    "username",
    "real_name",
    "chat_id"
))

#
# Глобальная переменная
#

Lobby = {}

#
# Вспомогательная переменная
#

cologa = [
[2, 'двойка', 'черви'], [2, 'двойка', 'крести'], [2, 'двойка', 'треф'], [2, 'двойка', 'буби'], 
[3, 'тройка', 'черви'], [3, 'тройка', 'крести'], [3, 'тройка', 'треф'], [3, 'тройка', 'буби'], 
[4, 'четвёрка', ' черви'], [4, 'четвёрка', 'крести'], [4, 'четвёрка', 'треф'], [4, 'четвёрка', 'буби'], 
[5, 'пятёрка', 'черви'], [5, 'пятёрка', 'крести'], [5, 'пятёрка', 'треф'], [5, 'пятёрка', 'буби'], 
[6, 'шестёрка', 'черви'], [6, 'шестёрка', 'крести'], [6, 'шестёрка', 'треф'], [6, 'шестёрка', 'буби'], 
[7, 'семёрка', 'черви'], [7, 'семёрка', 'крести'], [7, 'семёрка', 'треф'], [7, 'семёрка', 'буби'], 
[8, 'восьмерка', 'черви'], [8, 'восьмерка', 'крести'], [8, 'восьмерка', 'треф'], [8, 'восьмерка', 'буби'],
[9, 'девятка', 'черви'], [9, 'девятка', 'крести'], [9, 'девятка', 'треф'], [9, 'девятка', 'буби'], 
[10, 'десятка', 'черви'], [10, 'десятка', 'крести'], [10, 'десятка', 'треф'], [10, 'десятка', 'буби'],
[11, 'валет', 'черви'], [11, 'валет', 'крести'], [11, 'валет', 'треф'], [11, 'валет', 'буби'],
[12, 'дама', 'черви'], [12, 'дама', 'крести'], [12, 'дама', 'треф'], [12, 'дама', 'буби'],
[13, 'король', 'черви'], [13, 'король', 'крести'], [13, 'король', 'треф'], [13, 'король', 'буби'],
[14, 'туз', 'черви'], [14, 'туз', 'крести'], [14, 'туз', 'треф'], [14, 'туз', 'буби']]

#
# Вспомогательные функции
#

def _send_text(bot, user, text):
    bot.send_message(chat_id=user.chat_id, text=text)

def _send_md(bot, user, text):
    bot.send_message(chat_id=user.chat_id, text=text, parse_mode=ParseMode.MARKDOWN)

def message_all(bot, lobby:str, text:str):

	for i in range(len(Lobby[lobby]['Players'])):

		_send_text(bot, Lobby[lobby]['Players'][i]['info'], text)

def points_players(bot, lobby:str):

	for i in range(len(Lobby[lobby]['Players'])):

		_send_text(bot, Lobby[lobby]['Players'][i]['info'], 'У вас {}'. format(Lobby[lobby]['Players'][i]['point']))

def cologa_stir(cologa:list) -> list:

	num = randint(10, 26)

	for g in range(num):

		a = randint(5, 26)

		for i in range(a):

			d = cologa[a + i]

			cologa[a + i] = cologa[i]

			cologa[i] = d

	return cologa

def equalize(bot, Lobby_name: str):

	ante = Lobby[Lobby_name]['ante']

	Lobby[Lobby_name]['end'] += 1

	if ante > 0:

		if Lobby[Lobby_name]['Acting']['point'] <= ante:

			Lobby[Lobby_name]['Bank'] += Lobby[Lobby_name]['Acting']['point']

			Lobby[Lobby_name]['Acting']['point'] = 0

			Lobby[Lobby_name]['ва-банк'] = True

			message_all(bot, Lobby_name, 'Игрок {} пошёл ва-банк, чтобы уравнять ставку {}'. format(Lobby[Lobby_name]['Acting']['info'].real_name, ante))
			message_all(bot, Lobby_name, 'В банке {}'. format(Lobby[Lobby_name]['Bank']))

		else:

			Lobby[Lobby_name]['Acting']['point'] -= ante

			Lobby[Lobby_name]['Bank'] += ante

			message_all(bot, Lobby_name, 'Игрок {} уравнял ставку {}'. format(Lobby[Lobby_name]['Acting']['info'].real_name, ante))
			_send_text(bot, Lobby[Lobby_name]['Acting']['info'], 'У вас {}'. format(Lobby[Lobby_name]['Acting']['point']))

def raise_stake(bot, stake:int, Lobby_name:str):

	Lobby[Lobby_name]['ante'] = stake
	Lobby[Lobby_name]['Acting']['point'] -= stake
	Lobby[Lobby_name]['Bank'] += stake
	Lobby[Lobby_name]['end'] = 1
	message_all(bot, Lobby_name, 'Игрок {}({}) повысил ставку\nТеперь текущая ставка равна {}'.format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Acting']['info'].real_name, Lobby[Lobby_name]['ante']))

def all_in(bot, Lobby_name:str):

	Lobby[Lobby_name]['ва-банк'] = True
	Lobby[Lobby_name]['ante'] = Lobby[Lobby_name]['Acting']['point']
	Lobby[Lobby_name]['Bank'] += Lobby[Lobby_name]['Acting']['point']
	Lobby[Lobby_name]['Acting']['point'] = 0
	Lobby[Lobby_name]['end'] = 1
	message_all(bot, Lobby_name, 'Игрок №{}({}) пошёл ва-банк'.format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Acting']['info'].real_name))

def pass_play(bot, Lobby_name:str):

	Lobby[Lobby_name]['pass'].append(Lobby[Lobby_name]['Round_play'])
	Lobby[Lobby_name]['end'] += 1
	message_all(bot, Lobby_name, 'Игрок №{}({}) пас'.format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Acting']['info'].real_name))

def final_play(bot, Lobby_name:str):

	Lobby[Lobby_name]['Acting'] = None

	final = []

	for i in range(len(Lobby[Lobby_name]['Players'])):

		if i in Lobby[Lobby_name]['pass']:
			continue

		final.append(combo(Lobby[Lobby_name]['Players'][i]['cards'], Lobby[Lobby_name]['other']))
		final[-1].append(i)

		message_all(bot, Lobby_name, 'У игрока №{}({}) {}'. format(i + 1, Lobby[Lobby_name]['Players'][i]['info'].real_name, final[i][0]))

		message_all(bot, Lobby_name, 'Карты комбинации:')
		for j in range(len(final[i][1])):

			message_all(bot, Lobby_name, '{} {}'. format(final[i][1][j][1], final[i][1][j][2]))

		message_all(bot, Lobby_name, 'Старшая карта {} {}'. format(final[i][2][1], final[i][2][2]))

	max_combo = 0
	equal = []

	for i in range(1, len(final)):
		
		if final[max_combo][3] < final[i][3]:

			equal = []
			max_combo = i

		elif final[max_combo][3] == final[i][3]:

			check_1 = 0
			check_2 = 0

			if final[max_combo][1] in final[max_combo][2]:

				check_1 += 1

			if final[i][1] in final[i][2]:

				check_2 += 1

			if check_1 < check_2:

				max_combo = i

			elif check_1 == check_2:

				if final[max_combo][2][0] < final[i][2][0]:

					max_combo = i

				elif final[max_combo][2][0] == final[i][2][0]:

					equal.append(final[i][4])

	if len(equal) > 0:

		message_all(bot, Lobby_name, 'В этой партии несколько победителей, они разделят банк по ровну')

		message_all(bot, Lobby_name, 'Победители:')

		equal.append(final[max_combo][4])

		for i in range(len(equal)):

			message_all(bot, Lobby_name, '{}'. format(Lobby[Lobby_name]['Players'][equal[i]]['info'].real_name))

		Bank = Lobby[Lobby_name]['Bank'] // len(equal)

		for i in range(len(equal)):
			
			Lobby[Lobby_name]['Players'][equal[i]]['point'] += Bank

	else:

		message_all(bot, Lobby_name, 'Поздравляем Игрока №{} ({}), он выиграл в этом партии!'. format(final[max_combo][4] + 1, Lobby[Lobby_name]['Players'][final[max_combo][4]]['info'].real_name))

		Lobby[Lobby_name]['Players'][final[max_combo][4]]['point'] += Lobby[Lobby_name]['Bank']

	points_players(bot, Lobby_name)
	
	losers = []

	for i in range(len(Lobby[Lobby_name]['Players'])):
		
		if Lobby[Lobby_name]['Players'][i]['point'] == 0:
			message_all(bot, Lobby_name, 'Из-за потери всех очков, нашу комнату покидает Игрок {}({})'. format(i + 1, Lobby[Lobby_name]['Players'][i]['info'].real_name))
			losers.append(i)

	for j in range(len(losers)):

		del Lobby[Lobby_name]['Players'][losers[j]]

	if len(Lobby[Lobby_name]['Players']) == 1:

		_send_text(bot, Lobby[Lobby_name]['Creator'], '{}'.format(Lobby))

		_send_text(bot, Lobby[Lobby_name]['Players'][0]['info'], '{}, Поздравляем вас с полной победой\nТроекратное "ура" в честь победителя'. format(Lobby[Lobby_name]['Players'][0]['info'].real_name))
		_send_text(bot, Lobby[Lobby_name]['Players'][0]['info'], 'УРА!!!')
		_send_text(bot, Lobby[Lobby_name]['Players'][0]['info'], 'УРА!!!')
		_send_text(bot, Lobby[Lobby_name]['Players'][0]['info'], 'УРА!!!')

		del Lobby[Lobby_name]#НАКОНЕЦ-ТО!!!

	else:

		_send_md(bot, Lobby[Lobby_name]['Creator'], 'Чтобы запустить новую партию, напишите команду `/start_play {}`'. format(Lobby_name))

def _get_user(update):
    return User(
        update.message.from_user.id,
        update.message.from_user.username,
        update.message.from_user.full_name,
        update.message.chat_id
    )

def _save():
	dict_save = {}

	for i in Lobby:

		dict_save[i] = {'Creator': [
		Lobby[i]['Creator'].id,
		Lobby[i]['Creator'].username,
		Lobby[i]['Creator'].real_name,
		Lobby[i]['Creator'].chat_id
		]}

		dict_save[i]['Players'] = []

		for g in range(len(Lobby[i]['Players'])):

			dict_save[i]['Players'].append({})

			dict_save[i]['Players'][g]['info'] = [
			Lobby[i]['Players'][g]['info'].id,
			Lobby[i]['Players'][g]['info'].username,
			Lobby[i]['Players'][g]['info'].real_name,
			Lobby[i]['Players'][g]['info'].chat_id]

			for j in Lobby[i]['Players'][g]:

				if j == 'info':
					continue

				dict_save[i]['Players'][g][j] = Lobby[i]['Players'][g][j]

		for g in Lobby[i]:

			if g == 'Players' or g == 'Creator':
				continue

			dict_save[i][g] = Lobby[i][g]

	with open('Save.yaml', 'w') as file:

		file.write(yaml.dump(dict_save, Dumper = yaml.CDumper))

def _start():
	global Lobby

	with open('Save.yaml', 'r') as file:

		data = file.read()

		if data:

			Lobby = yaml.load(data, Loader = yaml.CLoader)

			for i in Lobby:

				Lobby[i]['Creator'] = User(
				Lobby[i]['Creator'][0],
				Lobby[i]['Creator'][1],
				Lobby[i]['Creator'][2],
				Lobby[i]['Creator'][3])

				for g in range(len(Lobby[i]['Players'])):

					Lobby[i]['Players'][g]['info'] = User(
					Lobby[i]['Players'][g]['info'][0],
					Lobby[i]['Players'][g]['info'][1],
					Lobby[i]['Players'][g]['info'][2],
					Lobby[i]['Players'][g]['info'][3])

#
# Команды
#

def start(bot, update):

	me = _get_user(update)

	_send_md(bot, me, 'Здравствуйте {}\nЯ покер-бот - помощник для проведения карточной игры "Покер"'. format(me.real_name))
	_send_md(bot, me, 'Если вы хотите создать комнату для игры `/create "название_комната" "тип игры"`\nНазвание комната должно содержать ОДНО слово\nТипы игры: \n1: по 100 очков у игроков \n2: по 200 очков у игроков\n3: по 300 очков у игроков')
	_send_md(bot, me, 'Если вы хотите присоединиться к уже созданной комнате `/join "название лобби" `')

def create(bot, update, args):

	me = _get_user(update)

	if not args:

		_send_md(bot, me, 'Введите название комнаты')
		return

	if len(args) != 2:

		_send_text(bot, me, 'Неверно создание комнаты\nВозможно вы не ввели название комната или тип игры, или же ввели название, содержащие более 1 одного слова')
		return

	if args[1] == '1':

		point = 100

	elif args[1] == '2':

		point = 200

	elif args[1] == '3':

		point = 300

	else:

		_send_text(bot, me, 'Неверно введён тип игры\nПопробуйте вести заново')
		return

	Lobby_name = args[0]

	if Lobby_name in Lobby:

		_send_text(bot, me, 'К сожалению это название уже занято\nПопробуйте ввести другое название')
		return

	cologa_play = cologa_stir(cologa)

	Lobby[Lobby_name] = {'Creator': me,
	'Players': [
	{'info': me,
	'point': point},

	{'info': me,
	'point': point}],

	'Acting': None,
	'Round': 0,
	'Round_play': 0,
	'cologa': cologa_play,
	'ante': 0,
	'point_lobbi': point}

	_send_md(bot, me, 'Комната создана\nЧто бы присоединиться туда, надо написать команду `/join {}`\nНапишите это тем, кто хочет присоединиться в вашей игре'. format(Lobby_name))
	_send_md(bot, me, 'Как только все участники присоединиться, напишите команду `/start_play {}`'. format(Lobby_name))

	_save()

def join(bot, update, args):

	me = _get_user(update)

	if not args:

		_send_text(bot, me, 'Введите название комнаты')
		return

	Lobby_name = args[0]

	if Lobby_name not in Lobby:

		_send_text(bot, me, 'Такой комнаты у нас нет\nУточните название комнаты')
		return

	if Lobby[Lobby_name]['Acting'] != None:

		_send_text(bot, me, 'Вы опоздали, игра в этой комнате уже началась')
		return

	for i in range(len(Lobby[Lobby_name]['Players'])):

		if Lobby[Lobby_name]['Players'][i]['info'].id == me.id:

			_send_text(bot, me, 'Вы уже присоединились к комнате\nПрошу, дождитесь когда начнётся игра')
			return

	if len(Lobby[Lobby_name]['Players']) == 4:

		_send_text(bot, me, 'В комнате не осталось мест\nИзвините')
		return

	Lobby[Lobby_name]['Players'].append(
	{'info': me,
	'point': Lobby[Lobby_name]['point_lobbi']})

	_send_text(bot, me, 'Отлично, теперь ждите начала игры')

	_send_md(bot, Lobby[Lobby_name]['Creator'], 'К нам присоединился {}({})'. format(me.real_name, me.username))

	if len(Lobby[Lobby_name]['Players']) == 4:

		_send_md(bot, Lobby[Lobby_name]['Creator'], 'В комнате уже не осталось мест\nМожем начинать игру')

	_save()

def start_play(bot, update, args):

	me = _get_user(update)

	if not args:

		_send_text(bot, me, 'Введите название комнаты')
		return

	Lobby_name = args[0]

	if Lobby_name not in Lobby:

		_send_text(bot, me, 'Такой комнаты нет\nПопробуйте ввести название заново')
		return

	if me.id != Lobby[Lobby_name]['Creator'].id:

		_send_text(bot, me, 'Запустить игру может только создатель комнаты\nЕсли вы уже долго ждёте, попытайтесь с ним связаться {}'. format(Lobby[Lobby_name]['Creator'].username))
		return

	if len(Lobby[Lobby_name]['Players']) < 2:

		_send_text(bot, me, 'В комнате должно быть как минимум 2 человека для игры\nНайдите ещё игроков')
		return

	if Lobby[Lobby_name]['Acting'] != None:

		_send_text(bot, me, 'Игра в этой комнате уже запущена')
		return

	message_all(bot, Lobby_name, 'Начало партии')

	Lobby[Lobby_name]['end'] = 2 if 2 + 1 <= len(Lobby[Lobby_name]['Players']) else 0
	Lobby[Lobby_name]['other'] = []
	Lobby[Lobby_name]['distribution'] = -1
	Lobby[Lobby_name]['Bank'] = 0
	Lobby[Lobby_name]['ва-банк'] = False
	Lobby[Lobby_name]['pass'] = []

	message_all(bot, Lobby_name, 'Список игроков:')
	for i in range(len(Lobby[Lobby_name]['Players'])):
		
		message_all(bot, Lobby_name, 'Игрок №{}({}), {} очков'. format(i + 1, Lobby[Lobby_name]['Players'][i]['info'].real_name, Lobby[Lobby_name]['Players'][i]['point']))

	for i in range(len(Lobby[Lobby_name]['Players'])):

 		Lobby[Lobby_name]['distribution'] += 2

 		Lobby[Lobby_name]['Players'][i]['cards'] = []

 		Lobby[Lobby_name]['Players'][i]['cards'].extend([Lobby[Lobby_name]['cologa'][Lobby[Lobby_name]['distribution'] - 1], Lobby[Lobby_name]['cologa'][Lobby[Lobby_name]['distribution']]])

 		_send_text(bot, Lobby[Lobby_name]['Players'][i]['info'], 'Вам раздали такие карты: {} {}, {} {}'. format(Lobby[Lobby_name]['Players'][i]['cards'][0][1], Lobby[Lobby_name]['Players'][i]['cards'][0][2], Lobby[Lobby_name]['Players'][i]['cards'][1][1], Lobby[Lobby_name]['Players'][i]['cards'][1][2]))

 		combo_player = combo(Lobby[Lobby_name]['Players'][i]['cards'], [])

 		_send_text(bot, Lobby[Lobby_name]['Players'][i]['info'], 'Комбинация {}, старшая карта {} {}'. format(combo_player[0], combo_player[2][1], combo_player[2][2]))

	Lobby[Lobby_name]['Round_play'] = Lobby[Lobby_name]['Round']

	Lobby[Lobby_name]['Round'] += 1

	Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['point'] -= 2

	message_all(bot, Lobby_name, 'Игрок под номером {}({}) выплачивает малый блайнд(2 очка)'. format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['info'].real_name))

	Lobby[Lobby_name]['Round_play'] = Lobby[Lobby_name]['Round_play'] + 1 if Lobby[Lobby_name]['Round_play'] + 2 <= len(Lobby[Lobby_name]['Players']) else 0

	Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['point'] -= 4

	Lobby[Lobby_name]['Bank'] += 6

	message_all(bot, Lobby_name, 'Игрок под номером {}({}) выплачивает большой блайнд(4 очка)'. format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['info'].real_name))
	points_players(bot, Lobby_name)
	message_all(bot, Lobby_name, 'В банке {}'. format(Lobby[Lobby_name]['Bank']))

	Lobby[Lobby_name]['Round_play'] = Lobby[Lobby_name]['Round_play'] + 1 if Lobby[Lobby_name]['Round_play'] + 2 <= len(Lobby[Lobby_name]['Players']) else 0

	Lobby[Lobby_name]['Acting'] = Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]

	message_all(bot, Lobby_name, 'Ход игрока №{}({})'. format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Acting']['info'].real_name))

	player = Lobby[Lobby_name]['Acting']

	_send_text(bot, player['info'], 'Ваши карты:\n{} {}\n{} {}'.format(player['cards'][0][1], player['cards'][0][2], player['cards'][1][1], player['cards'][1][2]))

	_send_text(bot, player['info'], 'Общие карты ещё не разданы')

	_send_text(bot, player['info'], 'Ваши действия:\n1:уравнять ставку/пропустить ставку\n2:поднять ставку\n3:ва-банк\n4:пас')

	_send_md(bot, player['info'], 'Введите номер вашего действия\nЕсли вы хотите поднять ставку напишите `2 "ставку"`')

	_save()


def action(bot, update):

	me = _get_user(update)
	message = update.message

	if message != None:

		if message.text[0] == '1' or message.text[0] == '2' or message.text[0] == '3' or message.text[0] == '4':

			check = False

			for i in Lobby:

				if Lobby[i]['Acting'] != None:

					if Lobby[i]['Acting']['info'].id == me.id:

						Lobby_name = i
						check = True
						break

			if check:

				if message.text[0] == '1':
		
					equalize(bot, Lobby_name)

				elif message.text[0] == '2':

					if len(message.text) < 2:

						_send_text(bot, me, 'Вы неправильно указали действие\nВозможно вы не указали ставку')
						return

					try:

						stake = int(message.text[2:])

					except ValueError as e:

						_send_text(bot, me, 'Вы неправильно указали ставку')
						return

					else:

						if stake >= Lobby[Lobby_name]['Acting']['point']:

							_send_text(bot, me, 'Ваша ставка превышает или равна ваши имеющие очки\nВведите ставку, которая меньше суммы ваших очков')
							return

						if stake <= Lobby[Lobby_name]['ante']:

							_send_text(bot, me, 'Ваша ставка ниже или равна текущей\nТекущая ставка {}\nВведите ставку, которая больше текущей'. format(Lobby[Lobby_name]['ante']))
							return

						raise_stake(bot, stake, Lobby_name)

				elif message.text[0] == '3':

					if Lobby[Lobby_name]['ante'] >= Lobby[Lobby_name]['Acting']['point']:

						_send_text(bot, me, 'Ваши очки не превышают текущую ставку\nУравняйте его ставку или идите в "пас"')
						return

					if Lobby[Lobby_name]['ва-банк'] == True:

						_send_text(bot, me, 'Один из игроков уже пошёл ва-банк\nУравняйте его ставку или идите в "пас"')
						return

					all_in(bot, Lobby_name)

				elif message.text[0] == '4':
					
					pass_play(bot, Lobby_name)

				message_all(bot, Lobby_name, 'В банке {}'. format(Lobby[Lobby_name]['Bank']))
				points_players(bot, Lobby_name)

				Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']] = Lobby[Lobby_name]['Acting']

				message_all(bot, Lobby_name, 'Ход закончен')

				if Lobby[Lobby_name]['ва-банк'] == True and Lobby[Lobby_name]['end'] == len(Lobby[Lobby_name]['Players']):

					message_all(bot, Lobby_name, 'Конец партии')
					if len(Lobby[Lobby_name]['other']) < 5:

						message_all(bot, Lobby_name, 'Раздача общих карт')

					for i in range(5 - len(Lobby[Lobby_name]['other'])):

						Lobby[Lobby_name]['distribution'] += 1

						Lobby[Lobby_name]['other'].append(Lobby[Lobby_name]['cologa'][Lobby[Lobby_name]['distribution']])

					message_all(bot, Lobby_name, 'Общие карты:')

					for i in range(len(Lobby[Lobby_name]['other'])):
						
						message_all(bot, Lobby_name, '{} {}'. format(Lobby[Lobby_name]['other'][i][1], Lobby[Lobby_name]['other'][i][2]))

					final_play(bot, Lobby_name)

			
					return

				quest = False

				for i in range(Lobby[Lobby_name]['Round_play'] + 1, len(Lobby[Lobby_name]['Players'])):
						
					if i not in Lobby[Lobby_name]['pass']:

						Lobby[Lobby_name]['Round_play'] = i
						quest = True
						break

				if not quest:

					for i in range(Lobby[Lobby_name]['Round_play']):
						
						if i not in Lobby[Lobby_name]['pass']:

							Lobby[Lobby_name]['Round_play'] = i
							quest = True
							break

				if len(Lobby[Lobby_name]['pass']) + 1 == len(Lobby[Lobby_name]['Players']):

					Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['point'] += Lobby[Lobby_name]['Bank']
					message_all(bot, Lobby_name, 'Все игроки, кроме {}, вышли из игры, следовательно весь банк переходит к игроку №{}({})'.format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]['info'].real_name))
					_send_md(bot, Lobby[Lobby_name]['Creator'], 'Чтобы запустить новую партию, напишите команду `/start_play {}`'. format(Lobby_name))

			
					return

				if Lobby[Lobby_name]['end'] == len(Lobby[Lobby_name]['Players']):

					Lobby[Lobby_name]['ante'] = 0
					Lobby[Lobby_name]['end'] = 0

					if len(Lobby[Lobby_name]['other']) == 0:

						message_all(bot, Lobby_name, 'Раздача общих карт')

						for i in range(3):

							Lobby[Lobby_name]['distribution'] += 1

							Lobby[Lobby_name]['other'].append(Lobby[Lobby_name]['cologa'][Lobby[Lobby_name]['distribution']])

						message_all(bot, Lobby_name, 'Общие карты:\n{} {}\n{} {}\n{} {}'. format(Lobby[Lobby_name]['other'][0][1], Lobby[Lobby_name]['other'][0][2], Lobby[Lobby_name]['other'][1][1], Lobby[Lobby_name]['other'][1][2], Lobby[Lobby_name]['other'][2][1], Lobby[Lobby_name]['other'][2][2]))

					elif len(Lobby[Lobby_name]['other']) >= 3 and len(Lobby[Lobby_name]['other']) < 5:

						message_all(bot, Lobby_name, 'Раздача общих карт')

						Lobby[Lobby_name]['distribution'] += 1

						Lobby[Lobby_name]['other'].append(Lobby[Lobby_name]['cologa'][Lobby[Lobby_name]['distribution']])

						message_all(bot, Lobby_name, 'Общие карты:')

						for i in range(len(Lobby[Lobby_name]['other'])):
							
							message_all(bot, Lobby_name, '{} {}'. format(Lobby[Lobby_name]['other'][i][1], Lobby[Lobby_name]['other'][i][2]))

					elif len(Lobby[Lobby_name]['other']) == 5:

						final_play(bot, Lobby_name)

						return

				Lobby[Lobby_name]['Acting'] = Lobby[Lobby_name]['Players'][Lobby[Lobby_name]['Round_play']]

				message_all(bot, Lobby_name, 'Ход игрока №{}({})'. format(Lobby[Lobby_name]['Round_play'] + 1, Lobby[Lobby_name]['Acting']['info'].real_name))

				player = Lobby[Lobby_name]['Acting']

				_send_text(bot, player['info'], 'Ваши карты:\n{} {}\n{} {}'.format(player['cards'][0][1], player['cards'][0][2], player['cards'][1][1], player['cards'][1][2]))

				if len(Lobby[Lobby_name]['other']) == 0:

					_send_text(bot, player['info'], 'Общие карты ещё не разданы')

				else:

					_send_text(bot, player['info'], 'Общие карты:')

					for i in range(len(Lobby[Lobby_name]['other'])):

						_send_text(bot, player['info'], '{} {}'. format(Lobby[Lobby_name]['other'][i][1], Lobby[Lobby_name]['other'][i][2]))

				player_combo = combo(Lobby[Lobby_name]['Acting']['cards'], Lobby[Lobby_name]['other'])

				_send_text(bot, player['info'], 'Ваша комбинация "{}"\nСтаршая карта "{} {}"'.format(player_combo[0], player_combo[2][1], player_combo[2][2]))

				if Lobby[Lobby_name]['ante'] > 0:

					_send_text(bot, player['info'], 'Текущая ставка {}'. format(Lobby[Lobby_name]['ante']))

				_send_text(bot, player['info'], 'Ваши действия:\n1:уравнять ставку/пропустить ставку\n2:поднять ставку\n3:ва-банк\n4:пас')

				_send_md(bot, player['info'], 'Введите номер вашего действия\nЕсли вы хотите поднять ставку напишите `2 "ставку"`')

		

#
# Главная функция
#

def main():
	_start()

	updater = Updater(BOT_TOKEN)

	updater.dispatcher.add_handler(CommandHandler("start", start))
	updater.dispatcher.add_handler(CommandHandler("create", create, pass_args=True))
	updater.dispatcher.add_handler(CommandHandler("join", join, pass_args=True))
	updater.dispatcher.add_handler(CommandHandler("start_play", start_play, pass_args=True))
	updater.dispatcher.add_handler(MessageHandler(None, action))

	if "PORT" in os.environ:
		updater.start_webhook(listen="0.0.0.0", port=int(os.environ["PORT"]), url_path=BOT_TOKEN)
		updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(BOT_APPNAME, BOT_TOKEN))
		print("Bot started on webhook")
	else:
		updater.start_polling()
		print("Bot started polling")

	updater.idle()

if __name__ == "__main__":
	main()
