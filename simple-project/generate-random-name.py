import requests
import random
base_url = 'https://salambae.pythonanywhere.com/api/v1/indonesia-general-name'
try:
    response = requests.get(base_url)
    response.raise_for_status()
    i = random.randint(0,99)
    print(f"{response.json()['data'][i]["firstName"]} {response.json()['data'][i]["lastName"]}")
except requests.exceptions.RequestException as e:
    print(f'Error request: {e}')