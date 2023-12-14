# import requests
# url="https://jsonplaceholder.typicode.com/todos/1"
# response=requests.get(url)
# gegevens=response.json()
# titel=gegevens['title'] 
# print(titel)

# status=gegevens['completed']
# if status==True:
#     print('Goed gedaan')
# else:
#     print('Er moet nog werk worden gedaan')

import requests
import webbrowser
from PIL import Image
from io import BytesIO

url = "https://dog.ceo/api/breeds/image/random"
response=requests.get(url)
gegevens=response.json()
foto=gegevens['message'] 
webbrowser.open(foto)

foto_response=requests.get(foto)
with open(r"C:\Users\Cursist\hond.jpg", "wb") as hond:
    hond.write(foto_response.content)
##Hieronder werk je met die import van PIL en io
# afbeelding = Image.open(BytesIO(foto_response.content))
# bestandsnaam = 'C:\\Users\Cursist\opgeslagen_afbeelding.jpg'
# afbeelding.save(bestandsnaam)
