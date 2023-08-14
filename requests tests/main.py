import requests

token = 'eb20d89c1861ebaa58790c3d4f633b6b'
host = 'https://api.pokemonbattle.me:9104'

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg',json = {
    "trainer_token": token,
    "email": "showoffdzy2j@qastudio.me",
    "password": "Iloveqa1"
}, headers = {'Content-Type': 'application/json'})'''


'''response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    'trainer_token': token
}, headers = {'Content-Type': 'application/json'})'''


'''response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Кит",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers = {'Content-Type': 'application/json',
              'trainer_token': token})'''


'''response_change_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6131",
    "name": "Cargo",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers= {'Content-Type': 'application/json',
              'trainer_token': token})'''

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json= {
    "pokemon_id": "6131"
}, headers={'Content-Type': 'application/json',
              'trainer_token': token})

print(response_add_pokeball.text)