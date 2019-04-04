import requests


def fetch_spacex_last_launch(url,path):    
    response = requests.get(url).json()
    latest_images = response['links']['flickr_images']
    
    for index,url_image in enumerate(latest_images):
        image = requests.get(url_image)
        image_name_tmpl = "images/spacex{}{}"
        image_name = image_name_tmpl.format(index,'.jpg')
        with open(image_name, 'wb') as file:
             file.write(image.content)
