import os
import pathlib
import fetch_hubble
import fetch_spacex
import insta


files_directory= "images/"
os.makedirs(directory, exist_ok=True)

url = 'https://api.spacexdata.com/v3/launches/latest'
fetch_spacex.fetch_spacex_last_launch(url,files_directory)

url = 'http://hubblesite.org/api/v3/image/{}'
fetch_hubble.fetch_hubble_images(url,files_directory,1)

insta.create_insta_post()





