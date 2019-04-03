import glob
import random
import time
from instabot import Bot

def create_insta_post()
    pics = glob.glob("./images/*.jpg")

    bot = Bot()
    bot.login(username=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
    for pic in pics:
        bot.upload_photo(pic)
        time.sleep(random.randint(1,5))
