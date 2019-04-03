import requests


def get_image_extension(url):
    image_url = url.split('.')
    return image_url[-1]

def fetch_hubble_images(url,path,image_id):  
    url = url.format(image_id)
    response = requests.get(url).json()
    hubble_image_urls = response['image_files']
    image_url = hubble_image_urls[-1]
    image_response = requests.get(image_url['file_url'])
    image_ext = get_image_extension(image_url['file_url'])
    image_name_tmp = "images/hubble.{}"
    image_name = image_name_tmp.format(image_ext)
    with open(image_name, 'wb') as file:
        file.write(image_response.content)
