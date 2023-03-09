import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200
    print(response.text)

@pytest.mark.parametrize('key, value', [('trainer_name', 'Персивальд Первый'), ('city', 'Псков')])

def test_name(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : '2154'})
    assert response.json()[key] == value