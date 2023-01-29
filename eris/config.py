import json
import os
## Config file

def get_user_list(config, key):
    with open("{}/eris/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    API_ID = 10843624
    STRING_SESSION = ""
    API_HASH = "733c7a9e356c9022cee2f2202bff99fe"
    CASH_API_KEY = "V7NS1NBFEL4X24L6"
    DATABASE_URL = "postgresql://jfzutjnb:6JpoUKMvDyqSGCTOnzny1w1eIpTB5yhi@heffalump.db.elephantsql.com/jfzutjnb"
    EVENT_LOGS = (-1001451724150)
    SUPPORT_CHAT = "bloggerminds" 
    TOKEN = "5334073790:AAGL0NyrccfBKsZ9oXF7yA9BKqccRtcmLEQ"
    TIME_API_KEY = "2AS711XS1O9B"
    OWNER_ID = 1356469075 
    ASSISTANT_ID = 5480870128
    WEATHER_API = "e8c43576833a8867d24a4e6785349e20"
    SPAMWATCH_API = "Xf1wOj5ZQY3kFQ60TtTX606G1LgHibVohI2~KxjHG5UjpVJS3HiZbb9ckbcherit"

    # Optional fields
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    BL_CHATS = []  # List of groups that you want blacklisted

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./cache"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
