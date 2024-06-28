# How can you use this API ?
- Write the code to interact with the API
```Python
import requests
base_url = 'https://salambae.pythonanywhere.com/api/v1/indonesia-general-name'
try:
    response = requests.get(base_url)
    response.raise_for_status()
    for i in range(99):
        print(f"{response.json()['data'][i]["firstName"]} {response.json()['data'][i]["lastName"]}")

except requests.exceptions.RequestException as e:
    print(f'Error request{e}')
```
# Example usage

#
