import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWNLOAD_LOCATION = "downloads"

Config.AUTH_USERS = [1451257129, 5480563272, 1753780498]
Config.API_ID = 5441410
Config.API_HASH = "a1a4fe7d23328f419d98a58339fd9980"
Config.BOT_TOKEN = "5199070719:AAHASnW4mOirKH1Nmq0d6vWP4G1Z_Pw5pXs"
Config.REDIS_HOST = "redis-17161.c270.us-east-1-3.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "wIW3pfcwu2UXkkNzsOpRsuX4OomCcexE"
REDIS_PORT = "17161"
