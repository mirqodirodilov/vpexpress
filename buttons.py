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
		contact = "Bizning raqamlar"
		price = 'Narxlar'
		otchot = 'Foto malumotlar'
		menu = 'Bosh menu'
		back = 'ortga'
	else:
		place = "Наш адрес 📍"
		id_number = "получить ID номер"
		contact = "Наши номера"
		price = 'Цены'
		otchot = 'Фото отчет'
		menu = 'Главное меню'
		back = 'назад'

	btn1 = KeyboardButton(place)
	btn2 = KeyboardButton(id_number)
	btn3 = KeyboardButton(contact)
	btn4 = KeyboardButton(price)
	btn5 = KeyboardButton(back)
	btn6 = KeyboardButton(menu)
	btn7 = KeyboardButton(otchot)
	markup.add(btn1,btn2,btn3,btn4,btn7)
	markup.row(btn5,btn6) 
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
				InlineKeyboardButton(text='https://t.me/vpexspressotchet',url='https://t.me/vpexspressotchet'),
			],

		],
	)
	return uztext
