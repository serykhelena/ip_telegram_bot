import telebot
import socket

with open('bot_token.txt', 'r') as vip_file:
    TOKEN = vip_file.read()

UNICORN_STICKER = "CAADAgAD5wIAAkcVaAnnQcbyzCQWrhYE"
NOT_WORKING_STICKER = "AAQCAAMNAwAChmBXDmIhZ5pao3rFmOCaDwAEAQAHbQADHVkAAhYE"

if TOKEN == 0:
    print("No token at all")

bot = telebot.TeleBot(TOKEN)

print("Ok")

@bot.message_handler(commands=['ip'])
def command_start(message):
    hostname = socket.gethostname()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    bot.reply_to(message,
                 'Hello, I\'m a demo IP Teller bot!\n'
                 'NUC Machine Name is: ' + hostname + '\n'
                 'NUC IP Address is: ' + s.getsockname()[0]
                 )
    bot.send_sticker(message.chat.id, UNICORN_STICKER)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    print(message.sticker)

if __name__ == '__main__':
    bot.polling(none_stop=True)