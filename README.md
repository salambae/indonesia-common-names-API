# Getting Started
- Write the code to interact with the API, Example:


# Example usage
1. Here's an example of how to access the API (using Python):
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
2. Using command prompt:
   ```Prompt
   curl https://salambae.pythonwhere.com/api/v1/indonesia-general-name
   ```
#
