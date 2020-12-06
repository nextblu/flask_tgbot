from flask import current_app, _app_ctx_stack
from .exceptions import TelegramBotTokenError
from pyrogram import Client


class TelegramBot:
    def __init__(self, bot_token, app=None):
        self.app = app
        self.bot_token = bot_token
        if not bot_token:
            raise TelegramBotTokenError("A bot token must be provided to start a bot.")
        if app:
            self.init_app(app)
        self.__client = Client(bot_token=self.bot_token)
