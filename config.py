#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7759243527:AAGlxLIgyS0b3CY_2I8zDNDI0qnw9ujz18k")
    API_ID = int(os.environ.get("API_ID", "29937683"))
    API_HASH = os.environ.get("API_HASH", "5f6d4ca9ffadd037db94446dc7c0d6fa")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6433733086")
