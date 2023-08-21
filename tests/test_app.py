import pytest
from ..app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# def test_start_recording(client):
#     response = client.post('/start')
#     assert response.status_code == 200
#     assert response.data == b'Recording started'

# def test_stop_recording(client):
#     response = client.post('/stop')
#     assert response.status_code == 200
#     assert response.data == b'Recording stopped'

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'start.html' in response.data

def test_general_route(client):
    response = client.get('/general')
    assert response.status_code == 200
    assert b'general_info.html' in response.data

def test_general_post_route(client):
    response = client.post('/general/send')
    assert response.status_code == 200

def test_bio_route(client):
    response = client.get('/bio')
    assert response.status_code == 200
    assert b'bio.html' in response.data

def test_bio_post_route(client):
    response = client.post('/bio/send')
    assert response.status_code == 200

def test_exp_route(client):
    response = client.get('/exp')
    assert response.status_code == 200
    assert b'experience.html' in response.data

def test_exp_post_route(client):
    response = client.post('/exp/send')
    assert response.status_code == 200

def test_ed_route(client):
    response = client.get('/ed')
    assert response.status_code == 200
    assert b'education.html' in response.data

def test_ed_post_route(client):
    response = client.post('/ed/send')
    assert response.status_code == 200

def test_skill_route(client):
    response = client.get('/skill')
    assert response.status_code == 200
    assert b'skills.html' in response.data

def test_skill_post_route(client):
    response = client.post('/skill/send')
    assert response.status_code == 200

def test_interest_route(client):
    response = client.get('/interest')
    assert response.status_code == 200
    assert b'interests.html' in response.data

def test_interest_post_route(client):
    response = client.post('/interest/send')
    assert response.status_code == 200

def test_lang_route(client):
    response = client.get('/lang')
    assert response.status_code == 200
    assert b'languages.html' in response.data

def test_lang_post_route(client):
    response = client.post('/lang/send')
    assert response.status_code == 200

def test_quality_route(client):
    response = client.get('/quality')
    assert response.status_code == 200
    assert b'qualities.html' in response.data

def test_quality_post_route(client):
    response = client.post('/quality/send')
    assert response.status_code == 200

def test_final_route(client):
    response = client.get('/final')
    assert response.status_code == 200
    assert b'final.html' in response.data

def test_download_route(client):
    response = client.get('/final/data')
    assert response.status_code == 200
    assert b'name' in response.data
    assert b'address' in response.data
    assert b'bio' in response.data
    assert b'education' in response.data
    assert b'skills' in response.data
    assert b'experience' in response.data
    assert b'interests' in response.data
    assert b'languages' in response.data
    assert b'qualities' in response.data