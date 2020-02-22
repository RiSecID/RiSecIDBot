""" Userbot start point """

from importlib import import_module
from sys import argv
from os import execle

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The phone no. entered is incorrect' \
             '\n  Tip: Use country code (eg +44) along with num.' \
             '\n       Recheck your phone number'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("You are running RizkyBot")

LOGS.info("RizkyNot Telah Aktif! Silahkan Tes Ketik .on Di Chat Manapun.")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
