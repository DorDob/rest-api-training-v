import requests


def test_ping():                       
    r = requests.get('http://18.184.234.77:8080/ping')    # url / endpoint, wrzuciam w zmienną r to response z requestu
    assert r.status_code == 200       # i to sprawdzi , czy otrzymam  200
    assert r.text == "pong"           # wyciągam respons body -> r.text sprawdzę, czy zwróci nam tekst, bo nie żądamy content-type jsona


def test_ping_accept_json():
    r = requests.get('http://18.184.234.77:8080/ping',
                     headers = {"Accept":"application/json"})  
    assert r.status_code == 200
    assert "application/json" in r.headers [ "content-type"]  # konkretne pola tablicy z headerami
    assert r.text == '{"reply":"pong!"}'  #sprawdzę, czy zwróci nam tekst, który powinien zwrócić
© 2020 GitHub, Inc.
