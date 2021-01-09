import requests

url = 'https://api.pwnedpasswords.com/range/' + 'password123'
res = requests.get(url)

print(res)
