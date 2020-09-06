import time

import telebot
from telebot import types

from Scene1 import Scene1
from core.Player import Player
from core.Position import Position
from core.Renderers import SymbolRenderer, ImageRenderer

bot = telebot.TeleBot('1145939924:AAHoFbXPnuL_WvjyeYwDxbOBNjkdX-IKDB4')

players = {}
scene = Scene1()
scene.generate_map()


@bot.message_handler(commands=['start'])
def start_message(message):
    new_player = Player(message.from_user.username, scene.world_map)
    new_player.spawn(Position(0, 0, 3))
    players[message.from_user.id] = [new_player, None]
    renderer = SymbolRenderer()
    render1 = ImageRenderer()
    curmap_img = render1.render_map(new_player.cur_map, new_player.fov, new_player.position)
    curmap = renderer.render_map(new_player.cur_map, new_player.fov, new_player.position)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('/up')
    markup.add('/left', '/right')
    markup.add('/down')
    msg = bot.send_message(message.chat.id, "<code>" + curmap + "</code>", parse_mode='HTML', reply_markup=markup)
    msg1 = bot.send_photo(message.chat.id, curmap_img, reply_markup=markup)
    players[message.from_user.id][1] = msg.message_id


@bot.message_handler(commands=['up', 'down', 'left', 'right'])
def start_message(message):
    print(message)
    print(message.text)
    renderer = SymbolRenderer()
    render1 = ImageRenderer()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('/up')
    markup.add('/left', '/right')
    markup.add('/down')

    try:
        cur_player = players[message.from_user.id]
    except:
        bot.send_message(message.chat.id, 'You are not registered in game, type "/start"', parse_mode='HTML', reply_markup=markup)
        return

    if message.text == "/up":
        cur_player[0].move("UP")
    elif message.text == "/down":
        cur_player[0].move("DOWN")
    elif message.text == "/left":
        cur_player[0].move("LEFT")
    elif message.text == "/right":
        cur_player[0].move("RIGHT")

    cur_map = renderer.render_map(cur_player[0].cur_map, cur_player[0].fov, cur_player[0].position)
    curmap_img = render1.render_map(cur_player[0].cur_map, cur_player[0].fov, cur_player[0].position)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('/up')
    markup.add('/left', '/right')
    markup.add('/down')
    print(cur_player[1])
    bot.send_message(chat_id=message.chat.id, text="<code>" + cur_map + "</code>", parse_mode='HTML', reply_markup=markup)
    bot.send_photo(message.chat.id, curmap_img, reply_markup=markup)

while True:
    try:
        bot.polling()
    except Exception as e:
        print(e)
        time.sleep(5)
