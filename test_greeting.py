import requests
import pytest


NAME = "Doroa"   # stała

def test_greeting():                       
    r = requests.get(pytest.HOST +'/greeting')   
    assert r.status_code == 200       #  sprawdza czy otrzymamy rzeczywiście 200,
    assert r.json()['content'] == 'Hello, Stranger!'  

def test_greeting_by_name(): 
        r = requests.get(
            pytest.HOST + '/greeting',
            params = {'name' : NAME}      # wysylam query params, ktore chce dodac do URL {klucz : wartosc}
        )

        assert r.status_code == 200
        assert r.json()['content'] == f"Hello, {NAME}!"   #zeby operowac zawsze na obiekcie
