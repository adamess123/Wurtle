import requests


def fetch_random_word(api_url, api_key):
    while True:
        response = requests.get(api_url, headers={
            'X-Api-Key': api_key
        }).json()

        if len(response["word"]) == 5:
            word = response["word"].lower()
            return word
