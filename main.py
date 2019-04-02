import requests
import os
import pathlib
from instabot import Bot
import glob
import random
import time

def get_image_extension(url):
    image_url = url.split('.')
    return image_url[-1]

def fetch_hubble_images(url,path,image_id):  
    url = url.format(image_id)
    print(url)
    response = requests.get(url).json()
    hubble_image_urls = response['image_files']
    image_url = hubble_image_urls[-1]
    image_response = requests.get(image_url['file_url'])
    image_ext = get_image_extension(image_url['file_url'])
    image_name_tmp = "images/hubble.{}"
    image_name = image_name_tmp.format(image_ext)
    with open(image_name, 'wb') as file:
        file.write(image_response.content)

def fetch_spacex_last_launch(url,path):    
    response = requests.get(url).json()
    lstest_images = response['links']['flickr_images']
    
    count = 0
    for url_image in lstest_images:
        image = requests.get(url_image)
        image_name_tmp = "images/spacex{}{}"
        count+=1
        image_name = image_name_tmp.format(count,'.jpg')
        with open(image_name, 'wb') as file:
             file.write(image.content)



files_directory= "images/"
directory = os.path.dirname(files_directory)
if not os.path.exists(directory):
    os.makedirs(directory)

url = 'https://api.spacexdata.com/v3/launches/latest'
fetch_spacex_last_launch(url,files_directory)

url = 'http://hubblesite.org/api/v3/image/{}'
fetch_hubble_images(url,files_directory,1)

pics = glob.glob("./images/*.jpg")

bot = Bot()
bot.login(username=os.getenv("LOGIN"), password=os.getenv("PASSWORD"))
for pic in pics:
   
    bot.upload_photo(pic)
    time.sleep(rendom.randint(1,5))
