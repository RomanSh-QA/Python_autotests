import pytest
import requests

def test_status_code():
    token = 'cb88e4cbf41088f80f25bbdfd9895979'
    response = requests.get('https://pokemonbattle.me:9104/trainers', headers = {'trainer_token' : token})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : 3776})
    response_body = response.text
    assert response.json()['trainer_name'] == 'Rooo'