import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())
with open('post.json', 'w') as file:
    json.dump(response.json(), file, indent=4)