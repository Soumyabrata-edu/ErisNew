import json
import os
## Config file

def get_user_list(config, key):
    with open("{}/eris/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    API_ID = 26435831
    STRING_SESSION = "1BVtsOK8Bu0kHB4_XG00Ff8U3mNSjqN_TZNveW4biMjtAjdMvryqPHQM8lOM2hSVFsRtMxT9pgTyGTZQ32rT99UzEY36LbiHX5uK3lFr-KM7-bmScELnAhMtFFjlQGtSQOAtujBTx2CPblISclBP3nkWyyEoUxnMWVnkSZAc_o8bIayDmQm3dCKyDIQaifl8mlAb8EkCJjDlkafhzrQQn3dK0kHdE4SYzA8xfhSCLDwgH8IEXykv5Q2DCmTHOBGlvKm0kVfuIiuR6-JxkU6UGO0pTSZAiCWWlYX3Q3QVAaOwQrIQI1adxfeMlhHJ7oDo3DHgmbJFgf1CMcT9Ws9fC_IUvCEF-zP8="
    API_HASH = "a9e7433f261715ca39efa8ffdeaf8823"
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
    NO_LOAD = ["musictools","userbotjoin","activevoice"]
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./cache"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
