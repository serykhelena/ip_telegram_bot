#!/usr/bin/env python
import telebot
import socket
import logging
from pyspectator.processor import Cpu 
from psutil import sensors_temperatures


with open('./Repos/ip_telegram_bot/bot_token.txt', 'r') as vip_file:
    TOKEN = vip_file.read()

UNICORN_STICKER = "CAADAgADKQwAAiMhBQAB4UzwzHmfF30WBA"

if TOKEN == 0:
    print("No token at all")

bot = telebot.TeleBot(TOKEN)
# logger = telebot.logger

cpu = Cpu(monitoring_latency=1)

def getCPUtemperature():
    # temp Core 1 current 
    return sensors_temperatures()["coretemp"][1][1]
    
def getCPUload():
    return str(cpu.load)

@bot.message_handler(commands=['info'])
def command_start(message):
    hostname = socket.gethostname()
    # AF_INET for using IPv4 
    # SOCK_STREAM for TCP
    # SOCK_DGRAM for UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    # s.getsockname() return the socket's own address
    # zB. ('127.0.0.1', 10000)
    bot.reply_to(message,
                 'Hello, I\'m a demo IP Teller bot!\n'
                 'NUC Machine Name is: ' + hostname + '\n'
                 'NUC IP Address is: ' + s.getsockname()[0] + '\n'
                 'CPU temperature is: ' + str(getCPUtemperature()) + '\n'
                 'CPU load is: ' + getCPUload() + '\n'
                 )
    bot.send_sticker(message.chat.id, UNICORN_STICKER)

# just for fun 
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    print(message.sticker)

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=1)
    except Exception as e:
        logging.basicConfig(filename='ip_bot_log.log', filemode='a', 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logging.exception(e)