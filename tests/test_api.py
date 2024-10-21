import pytest

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200

def test_text_translation(client):
    data = {
        "text": "how are you?",
        "from": "en",
        "to": "jp"
    }
    response = client.post('/text', json=data)
    assert response.status_code == 200