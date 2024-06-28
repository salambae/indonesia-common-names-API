# Getting Started
- Write the code to interact with the API, Example:


# Example usage
### Here's an example of how to access the API (using Python):
All data from API will be read, no exception
```Python
import requests
base_url = 'https://salambae.pythonanywhere.com/api/v1/indonesia-general-name'
try:
    response = requests.get(base_url)
    response.raise_for_status()
    for i in range(99):
        print(f"{response.json()['data'][i]["firstName"]} {response.json()['data'][i]["lastName"]}")
except requests.exceptions.RequestException as e:
    print(f'Error request{e}'
```

### Accessing the API using command prompt:
Also, you can access the API from command prompt for example
```Prompt
   curl https://salambae.pythonwhere.com/api/v1/indonesia-general-name
```

### Generating random name:
Use ```randint()``` method for generating a random name, example:
```Python
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
```
