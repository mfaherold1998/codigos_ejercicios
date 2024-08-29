'''
* Crea un programa que se encargue de calcular el aspect ratio de una
* imagen a partir de una url.
* - Url de ejemplo:
*   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
* - Por ratio hacemos referencia por ejemplo a los "16:9" de una
*   imagen de 1920*1080px.
'''

import PIL.Image
import requests
from math import gcd 


url = 'https://img.freepik.com/foto-gratuito/bella-scena-dei-cartoni-animati-dei-personaggi-degli-anime_23-2151035157.jpg?t=st=1724964016~exp=1724967616~hmac=7db7bd8ec0e875998cba19a6b3186c9e192dc4a331d5449b5f6bc889f840c387&w=360'

img_data = requests.get(url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

img = PIL.Image.open('image_name.jpg')

mcd = gcd(img.width, img.height)
num = img.width//mcd
den = img.height//mcd

ratio = '{}:{}'.format(num, den)

print ( f'ratio: {ratio} size {img.size}' )
