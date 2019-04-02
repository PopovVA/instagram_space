import requests


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
