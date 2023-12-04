import datetime
import pytest
import requests


@pytest.fixture(autouse=True)
def init_cache(request):
    request.config.cache.get('tokens', None)


def test_create_user(request):
    body = {
        'email': 'test@test.ru',
        'password': '12345'
    }
    response = requests.post(f'http://127.0.0.1:8000/api/v1/user/register', data=body)
    assert response.status_code == 201
    if response.status_code == 201:
        data = response.json()
        request.config.cache.set('user', data)
    assert response.json()['email'] == body['email']


def test_get_tokens(request):
    body = {
        'email': 'test@test.ru',
        'password': '12345'
    }
    response = requests.post(f'http://localhost:8000/api/v1/user/login', data=body, timeout=5)
    assert response.status_code == 200
    if response.status_code == 200:
        data = response.json()
        request.config.cache.set('tokens', data)


def test_add_data(request):
    response = requests.get(f'http://localhost:8000/api/v1/test')
    assert response.status_code == 200
    assert response.json() == {"ok": "ok"}


def test_get_anonim_rates(request):
    response = requests.get(f'http://localhost:8000/api/v1/rates')
    assert response.status_code == 200
    assert response.json() is not None


def test_get_auth_rates(request):
    token = request.config.cache.get('tokens', None)['access']
    response = requests.get(f'http://localhost:8000/api/v1/rates', headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == []


def test_add_tracked_currency(request):
    body = {
        "currency": 1,
        "threshold": 100
    }
    token = request.config.cache.get('tokens', None)['access']
    response = requests.post('http://localhost:8000/api/v1/currency/user_currency', data=body,
                             headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    if response.status_code == 201:
        data = response.json()
        request.config.cache.set('tracked_currency', data)


def test_patch_tracked_currency(request):
    body = {
        "threshold": 110
    }
    currency_id = request.config.cache.get('tracked_currency', None)['currency']
    token = request.config.cache.get('tokens', None)['access']
    response = requests.patch(f'http://localhost:8000/api/v1/currency/user_currency/{currency_id}', data=body,
                              headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


def test_analytic(request):
    date_from = datetime.date.today()
    date_to = datetime.date.today() + datetime.timedelta(days=1)
    threshold = 90
    currency_id = request.config.cache.get('tracked_currency', None)['currency']
    token = request.config.cache.get('tokens', None)['access']
    response = requests.get(
        f'http://localhost:8000/api/v1/currency/{currency_id}/analytic?date_from={date_from}&date_to={date_to}&threshold={threshold}',
        headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() is not None


def test_delete_tracked_currency(request):
    currency_id = request.config.cache.get('tracked_currency', None)['currency']
    token = request.config.cache.get('tokens', None)['access']
    response = requests.delete(f'http://localhost:8000/api/v1/currency/user_currency/{currency_id}',
                               headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 204
