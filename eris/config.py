import json
import os
## Config file

def get_user_list(config, key):
    with open("{}/eris/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    API_ID = 25674865
    STRING_SESSION = "1BVtsOIcBu2-Sl3SZQ6id7fzqqsgWGbcXygivFS8Z_-V2vIlMFaY_qZl1ZhlSzHFnxq2RSTQZHsxacJm95rR1tFqSv4NGhlG-tpwkvoEbtIdf_foOJlj4GNYrDKcVaQvxEzQy65mVI3U3hhvnBDgFIzTC45YPTNo-p6zFTg_18cFGo8Zwp9G4E2UZswIlJTIBRkMZo-dFPto9Ea8-naTEvNcp-pQ-6sZjbGzZvDJr314l-IhNDdiFhvFxFZeTb1dq1mprirL3hEWMBeRsPKEA9euk6ExgcAWcJl1dcg4V8fZbsSMqteNwgtmV8aG3zJvxhQVntoOfB3zX5xVxUwuI4FPTwQ7qW30="
    API_HASH = "9d652fa93edd9fed18ed6bae41919f12"
    CASH_API_KEY = "V7NS1NBFEL4X24L6"
    DATABASE_URL = "postgresql://cevvmtjl:2LeJJUSH8QttXem2wklIVfFgxxvSyDv-@hattie.db.elephantsql.com/cevvmtjl"
    EVENT_LOGS = (-1001451724150)
    SUPPORT_CHAT = "bloggerminds" 
    TOKEN = "5334073790:AAGf4OGhRuZ5g7CPqK9mysedFwjIeCpOJlI"
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
    NO_LOAD = ["musictools"]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./cache"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
