#!/bin/bash

export http_proxy=http://10.128.0.100:8080/
export https_proxy=http://10.128.0.100:8080/
export HTTP_PROXY=http://10.128.0.100:8080/
export HTTPS_PROXY=http://10.128.0.100:8080/

cd /home/user-sau-nuc/Repos/ip_telegram_bot
source virtualenv/env/bin/activate
python3 bot.py
echo "Success" > bot.log
