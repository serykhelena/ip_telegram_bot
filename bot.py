import telebot

# for local machine 
with open('vip_file.txt', 'r') as vip_file:
    TOKEN = vip_file.read()

# for heroku
# TOKEN = os.getenv('TOKEN', 0)


if TOKEN == 0:
    print("No token at all")
bot = telebot.TeleBot(TOKEN)



if __name__ == '__main__':
    bot.polling(none_stop=True)