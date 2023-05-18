from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton,ReplyKeyboardMarkup
from texsts import *


til = ReplyKeyboardMarkup(
	keyboard =[
		[
			KeyboardButton("🇺🇿 Uzbek"),
		],
		[
			KeyboardButton("🇷🇺 Русский"),
		],
	],
	resize_keyboard=True
)

def get_started(lang):
	text = langs[lang]
	menuuz = ReplyKeyboardMarkup(resize_keyboard=True)
	btn = KeyboardButton(text[100])
	menuuz.add(btn)
	return menuuz




def main_nopka(lang):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	markup1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	if lang == "uz":
		place = "Bizning Manzil 📍"
		id_number = "ID raqam olish"
		price = 'Narxlar'
		otchot = 'Foto malumotlar'
		shtrix = "Tovarni ko'rish"
		errror = "Xatoliklarni to'g'irlash"
		back = 'ortga'
	else:
		place = "Наш адрес 📍"
		id_number = "получить ID номер"
		price = 'Цены'
		otchot = 'Фото отчет'
		shtrix = "Посмотреть продукт"
		errror = "Исправить ошибки"
		back = 'назад'

	btn1 = KeyboardButton(place)
	btn2 = KeyboardButton(id_number)
	btn4 = KeyboardButton(price)
	btn5 = KeyboardButton(back)
	btn7 = KeyboardButton(otchot)
	btn8 = KeyboardButton(shtrix)
	btn9 = KeyboardButton(errror)
	markup.row(btn1,btn2)
	markup.row(btn4,btn8) 
	markup.row(btn7,btn9) 
	markup.row(btn5) 
	return markup


	

country = ReplyKeyboardMarkup(
	keyboard =[
		[
			KeyboardButton("📍отправить адрес",),
		],

	],
	resize_keyboard=True
)

def t(lang):
	uztext = InlineKeyboardMarkup(
		inline_keyboard =[
			[
				InlineKeyboardButton(text='https://t.me/exspressotchet',url='https://t.me/exspressotchet'),
			],

		],
	)
	return uztext


