# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("35029722"))
    API_HASH = os.environ.get("271cd4b0f1df86ba25f2568182ad2691")
    BOT_TOKEN = os.environ.get("8277666643:AAFUkehS5w7n62ZkwEObye49t9B6O9a_vW4")
    LOGS_CHANNEL = int(os.environ.get("-1003728144531"))
    BOT_OWNER = int(os.environ.get("7192691902"))
    MONGODB_URL = os.environ.get("MONGODB_URL")
    GOFILE_TOKEN = os.environ.get("Q6EqgbN0VmcVqbNgs17AiGTvn7fTxU3Z")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
