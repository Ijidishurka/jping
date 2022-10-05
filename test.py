import random
import logging
from .. import loader, utils
from random import randint, choice

logger = logging.getLogger(__name__)


def register(cb):
    cb(pinj())


class pinj(loader.Module):
    """Фейк пинг"""
    strings = {'name': 'pinj by @modwini'}

    async def pinjcmd(self, message):
        """Используй .ping <цифры>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit('<b>Нет аргумента после команды-_- </b>')
            return
        else:
            pinj = ("⏱" + "<b> Скорость отклика Telegram: </b>" + f"<code>{text}</code>" + "<b> ms</b>" + " <b> \n😎 Прошло с последней перезагрузки: 3:59:27 \n</b>")

            await message.edit(pinj)