import os
import pathlib
import fetch_hubble
import fetch_spacex
import insta_post


files_directory= "images/"
directory = os.path.dirname(files_directory)
if not os.path.exists(directory):
    os.makedirs(directory)

url = 'https://api.spacexdata.com/v3/launches/latest'
fetch_spacex.fetch_spacex_last_launch(url,files_directory)

url = 'http://hubblesite.org/api/v3/image/{}'
fetch_hubble.fetch_hubble_images(url,files_directory,1)

insta_post.insta_post()





