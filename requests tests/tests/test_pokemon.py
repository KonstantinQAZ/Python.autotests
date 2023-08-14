import requests
import pytest

token = 'eb20d89c1861ebaa58790c3d4f633b6b'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': '2007'})
    assert response.json()['trainer_name'] == 'Кит'