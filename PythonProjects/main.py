import requests

token = 'e100b308851e63f5d37cbd8c9bd086be'

response = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
})

print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id,
    "name": "Корень",
    "photo": ""
})

print(response_change.text)

response_catch = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 'trainer_token' : token},
json = {
    "pokemon_id": pokemon_id
})

print(response_catch.text)