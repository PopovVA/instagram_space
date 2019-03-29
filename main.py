import requests
import os
import pathlib


def get_image_extension(url):
    image_url = url.split('.')
    return image_url[-1]

def fetch_hubble_images(url,path):  
    response = requests.get(url).json()
    hubble_image_urls = response['image_files']
    count = 0
    for url in hubble_image_urls:
        image = requests.get(url['file_url'])
        image_ext = get_image_extension(url['file_url'])
        image_name_tmp = "images/hubble{}.{}"
        count+=1
        image_name = image_name_tmp.format(count,image_ext)
        with open(image_name, 'wb') as file:
             file.write(image.content)

def fetch_spacex_last_launch(url,path):    
    response = requests.get(url).json()
    #print(response)
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

url = 'http://hubblesite.org/api/v3/image/1'
fetch_hubble_images(url,files_directory)



