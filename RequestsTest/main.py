import requests

response = requests.post('https://pokemonbattle.me:9104/trainers/reg',json= {
    "trainer_token": "cb88e4cbf41088f80f25bbdfd9895979",
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
})
print(response.status_code)
token = 'cb88e4cbf41088f80f25bbdfd9895979'

response_activated = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
})

#Создание покемона
response_add_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'trainer_token' : token}, json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
} )
print(response_add_pokemon.text)

#Смена имени покемон
response_change_name = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'trainer_token' : token}, json = {
    "pokemon_id": "8896",
    "name": "Bulbazavr",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_change_name.text)

#Поймать покемона в покебол
response_catch_pokemon = requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball', headers = {'trainer_token' : token}, json = {
    "pokemon_id": "8896"
})
print(response_catch_pokemon.text)