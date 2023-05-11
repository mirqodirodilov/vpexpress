import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from bot_commands import *
from funk import *
from aiogram.types import BotCommand, BotCommandScopeDefault, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from geopy.geocoders import Nominatim
from aiogram.types import ContentType,Message
from state import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from googletrans import Translator


API_TOKEN = '5993319262:AAEcaxFhaKUA-rWrGIjR6F1cSYAtJPj9sHA'

admin = 708006401
admin1 = 276491503
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())






db = Tablitsa()
translator = Translator()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    conn = sqlite3.connect("china.db")
    c = conn.cursor()
    user_id = message.from_user.id
    db.create_table()
    c.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
    data = c.fetchone()
    if data is None:
        c.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id) )
        conn.commit()
        await message.reply(f"*Assalomu aleykum {username}\nVp expressuz_botimizga Xush kelibsz ☺️\n\nTilni tanlang Выберите язык👇*",parse_mode='markdown',reply_markup=til)
        await set_all_default_commands(bot)
    else:
        await message.answer("*Siz ro'yxatdan o'tkansz ✅\n\nВы зарегистрированы ✅*",parse_mode='markdown',reply_markup=til)
        await set_all_default_commands(bot)


############################################################################ LANGUAGE
@dp.message_handler(lambda message: message.text in ["🇺🇿 Uzbek", "🇷🇺 Русский"])
async def choose_lang(message: types.Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    admin = '708006401'
    test = db.select_main(admin)
    uzb_text = test[5]
    ru_text = test[6]
    if message.text == "🇺🇿 Uzbek":
            lang = 'uz'
            text = "*Assalomu alaykum Vp Express kuryeri tovarlarni bizning omborimizga kelganidan keyin 5 kun - 12 kun ichida yetkazib beradi. Nega biz bilan ishlayapsiz?\n\n1. Xushmuomalalik\n2. 24/7 sizning xizmatingizda va yangiliklar, qaysi kunlarni mag'lub etishni va mag'lub qilmaslikni taklif qiladi\n3. Bonuslar va chegirmalar oling\n4. Omborga har bir tovar qabul qilish uchun 100% javobgarlik\n5. Arzon narxda sifatli va tez yetkazib berish*"
            text_1 = f"*{uzb_text}*"
    elif message.text == "🇷🇺 Русский":
            lang = 'ru'
            text = "*Мир вам Курьер Vp Express доставит груз в течение 5 дней - 12 дней после прибытия на наш склад. Почему вы работаете с нами?\n\n1. Вежливость\n2. 24/7 к вашим услугам и новости, подсказывающие, в какие дни бить и не бить\n3. Получайте бонусы и скидки\n4. 100% ответственность за каждое поступление товара на склад\n5. Хорошее качество и быстрая доставка по низкой цене *"
            text_1 = f"*{ru_text}*"
    db.update_lang(lang, from_user_id)
    admin = '708006401'
    image = db.select_video(admin)
    for i in image:
        try:
            await message.answer(text, parse_mode='markdown',reply_markup=main_nopka(lang))
            await message.answer_video(i,caption=text_1,parse_mode='markdown')
        except:
            await message.answer_photo(i,caption=text_1,parse_mode='markdown')
############################################################################ LANGUAGE


@dp.message_handler(lambda message: message.text in ['получить ID номер', 'ID raqam olish'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*ID raqam olish uchun sizdan kerak boladigan hujjatlar📄❗\n\n1.Pasport ✅\n2.Doim aloqada boladigan raqam ✅\n3.Mahsulotni yetkazib berish uchun yashash manzilingiz✅\n\nID raqam olish uchun @vpexspress_admin ga malumotlarni yuboring va sizga ID raqam beriladi ✅*"
    elif lang == 'ru':
        text = "*Документы необходимые для получения идентификационного номера📄❗\n\n1.Паспортный ✅\n2. Номер, с которым вы поддерживаете связь ✅\n3.Место проживание ✅\n\nОтправьте свои данные на @vpexspress_admin, чтобы получить идентификационный номер, и вам будет присвоен идентификационный номер.✅*"

    await message.answer(text, parse_mode='markdown')




################################################################################## TEL RAQAM

@dp.message_handler(lambda message: message.text in ['Наши номера', 'Bizning raqamlar'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*Telegram kanalimiz: https://t.me/vpexspres\nAdmin: @vpexspress_admin\nAdmin: +998 99 937 88 77\nManager: @vpexspress_manager\nManager: +998 97 783 22 44\nFoto-hisobotlar: https://t.me/vpexspressotchet*"
    elif lang == 'ru':
        text = "*Наш Telegram-канал: https://t.me/vpexspres\nАдминистратор: @vpexspress_admin \nAdmin: +998 99 937 88 77\nManager: @vpexspress_manager\nManager: +998 97 783 22 44 \nфото отчет: https://t.me/vpexspressotchet*"

    await message.answer(text, parse_mode='markdown')

########################################################################################### PRICE
@dp.message_handler(lambda message: message.text in ['Цены', 'Narxlar'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*1.Yuklar narxi 11$ dan xech qanday minimalkalarsiz *"
    elif lang == 'ru':
        text = "*1.Стоимость доставки начинается от 11$ долларов без минимума.*"
    await message.answer(text, parse_mode='markdown')


@dp.message_handler(lambda message: message.text in ['назад', 'ortga'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*Tilni tanlang 👇*"
    elif lang == 'ru':
        text = "*Выберите язык 👇*"

    await message.answer(text, parse_mode='markdown',reply_markup=til)


@dp.message_handler(lambda message: message.text in ['Главное меню', 'Bosh menu'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*Tilni tanlang 👇*"
    elif lang == 'ru':
        text = "*Выберите язык 👇*"

    await message.answer(text, parse_mode='markdown',reply_markup=til)


############################################################################ SEND LOCATION

@dp.message_handler(lambda message: message.text in ['Bizning Manzil 📍', 'Наш адрес 📍'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*Bizning manzil 📍 : 14 А Farobi ko'chasi, Tashkent*"
    elif lang == 'ru':
        text = "*Наш адрес 📍: г. Ташкент, ул. Фароби, 14 А*"
    await bot.send_location(chat_id=from_user_id,latitude = 41.347122,longitude = 69.19991)
    await message.answer(text=text,parse_mode='markdown')

@dp.message_handler(lambda message: message.text in ['Фото отчет', 'Foto malumotlar'])
async def send_id_number(message: types.Message):
    from_user_id = message.from_user.id
    lang = db.select_lang(from_user_id)[0]

    if lang == "uz":
        text = "*Foto malumotlar kanalimiz*"
    elif lang == 'ru':
        text = "*Наш канал фото отчет*"
    await message.answer(text=text,parse_mode='markdown',reply_markup=t(lang))



@dp.message_handler(commands=['update_media'])
async def send_welcome(message: types.Message):
    text = "*Rasm yoki Video jonating*"
    await bot.send_message(chat_id=admin,text=text,parse_mode='markdown')



@dp.message_handler(content_types=ContentType.PHOTO,state=None)
async def reaction_to_photo_video(message: types.Message):
    user_id = message.from_user.id
    photo_id = message.photo[-1].file_id
    db.update_video(photo_id,user_id)
    text = "*Rasm Yuklandi ✅ Textni kiriting*"
    await bot.send_message(chat_id=admin,text=text,parse_mode='markdown')
    await Royxat.text_desc.set()

@dp.message_handler(content_types=ContentType.VIDEO,state=None)
async def reaction_to_video(message: types.Message):
    user_id = message.from_user.id
    video_id = message.video.file_id
    db.update_video(video_id,user_id)
    text = "*Video Yuklandi ✅ Textni kiriting*"
    await bot.send_message(chat_id=admin,text=text,parse_mode='markdown')
    await Royxat.text_desc.set()



@dp.message_handler(state=Royxat.text_desc)
async def step_1(msg:types.Message,state:FSMContext):
    text_desc = msg.text
    text = '*finish ✅*'
    admin = '708006401'
    db.update_text(text_desc,admin)
    rest = translator.translate(text_desc, dest="ru")
    russ_text = rest.text
    db.update_textrus(russ_text,admin)
    await bot.send_message(chat_id=admin,text=text,parse_mode='markdown')
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)