import requests

# These code snippets use an open-source library. http://unirest.io/python
response = requests.get("https://wordsapiv1.p.mashape.com/words?random=true",
    headers={
    "X-Mashape-Key": "f974116797msh3d546fc58c8e9bfp185392jsn89d99727c669",
    "Accept": "application/json"
  }
)

print(response.json())
# word = response.json()['word'[0]]

# # if (word )
# print(word)