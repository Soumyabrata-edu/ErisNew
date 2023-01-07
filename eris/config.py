import json
import os

def get_user_list(config, key):
    with open("{}/eris/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    API_ID = 26435831
    STRING_SESSION = "1BVtsOMEBuzmTenWDK9tmMhdfcrgFZKIzkp0J2wsh8qcw9JD2EvSxMs1O3-HhMnGZu1ayhrigpwV53haKSi9AcCDDFGoh99uguJRP8o2ZEtxa_f_fdk-UBbYYAqQzfhoh00fBsBX5oMf3Xnd0bbWliR-S9vxuinirnbQa2FLDJvjmfiGUleXKt1Vrume1QPlA4Yj24hSFrJfPDUwOKFGeiNs5IftVm2LUnpqFAhw-A8XYIzxGCeed1hH8ZcSViFxO-AKc9MBt0E5jMvdWuTboR_KjnWQIqsZtHUhuSkCVaf6xdqSmZYHXVNavVFaCNnKsFjt2RuvzvWncC_kSTA583C1fjgHKAIQ="
    API_HASH = "a9e7433f261715ca39efa8ffdeaf8823"
    CASH_API_KEY = "V7NS1NBFEL4X24L6"
    DATABASE_URL = "postgresql://cevvmtjl:2LeJJUSH8QttXem2wklIVfFgxxvSyDv-@hattie.db.elephantsql.com/cevvmtjl"
    EVENT_LOGS = (-1001451724150)
    SUPPORT_CHAT = "bloggerminds" 
    TOKEN = "5334073790:AAFJbxGqno6AtqjG5_ZJAjibjTERBTeAM6M"
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
    NO_LOAD = ["special"]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True