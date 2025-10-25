import requests

def test_login_api(base_url):
    url = base_url + '/api/auth/login'
    resp = requests.post(url, json={'email':'testuser@example.com','password':'Password123'})
    assert resp.status_code == 200
    data = resp.json()
    assert 'token' in data
