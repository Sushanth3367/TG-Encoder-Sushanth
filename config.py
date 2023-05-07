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

Config.AUTH_USERS = [1930343434, 5126929234, -1001554444490, 1221558981]
Config.API_ID = 3281305
Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
Config.BOT_TOKEN = "5231542469:AAHgiw9C7W0epkmlek9k_AMBs_mwMlg2VUM"
Config.REDIS_HOST = "redis-17161.c270.us-east-1-3.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "wIW3pfcwu2UXkkNzsOpRsuX4OomCcexE"
REDIS_PORT = "17161"
