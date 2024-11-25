# https://t.me/pypfnhfhjbot
import telebot
import logicgame

bot = telebot.TeleBot("6600123455:AAFYfZV2BIR0WlU3HepJCMoZSPA_L8jmK9M")
CURRENT_PLAYER = ['X']


@bot.message_handler(commands=['start'])
def start_game(message):
    logicgame.clear_data()
    bot.send_message(message.chat.id, f'Новая игра началась:')
    bot.send_message(message.chat.id,logicgame.print_game_field())
    bot.send_message(message.chat.id,f"Ваш ход: {CURRENT_PLAYER[0]}")


@bot.message_handler(content_types=['text'])
def start_game(message):
    bot.send_message(
        message.chat.id,
        logicgame.input_value(message.text, CURRENT_PLAYER[0])
    )
    if logicgame.check_is_game_end() == logicgame.STATUS_CONTINUE:
        bot.send_message(
            message.chat.id,
            logicgame.print_game_field()
        )
        if CURRENT_PLAYER[0] == 'X':
            CURRENT_PLAYER[0] = 'O'
        else:
            CURRENT_PLAYER[0] = 'X'
        bot.send_message(
            message.chat.id,
            f"Ваш ход: {CURRENT_PLAYER[0]}"
        )
    else:
        bot.send_message(message.chat.id, f"Игра окончена, победа: {logicgame.check_is_game_end()}")


bot.infinity_polling()