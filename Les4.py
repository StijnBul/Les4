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



# import requests
# import webbrowser
# from PIL import Image
# from io import BytesIO
# url = "https://dog.ceo/api/breeds/image/random"
# response=requests.get(url)
# gegevens=response.json()
# foto=gegevens['message'] 
# webbrowser.open(foto)
# foto_response=requests.get(foto)
# with open(r"C:\Users\Cursist\hond.jpg", "wb") as hond:
#     hond.write(foto_response.content)
##Hieronder werk je met die import van PIL en io
## afbeelding = Image.open(BytesIO(foto_response.content))
## bestandsnaam = 'C:\\Users\Cursist\opgeslagen_afbeelding.jpg'
## afbeelding.save(bestandsnaam)



# import requests
# naam = str(input('Wat is je naam?'))
# keuze = str(input(f'{naam}, wil je een mopje horen? '))
# if keuze == 'ja':
#     url="https://moppenbot.nl/api/random/"
#     response=requests.get(url)
#     gegevens=response.json()
#     mop=gegevens['joke']['joke']
#     print(mop)
# else:
#     print('The jokes on you!')



import requests
onderwerp=str(input('Waarover wil je iets meer weten?'))
url="https://newsapi.org/v2/everything?q="+onderwerp+"&from=2023-11-14&sortBy=publishedAt&apiKey=e48c49081778415ebb75433c54d61ac9"
response=requests.get(url)
gegevens=response.json()
for titel in gegevens['articles']:
        print(f"Titels: {titel['title']}")
