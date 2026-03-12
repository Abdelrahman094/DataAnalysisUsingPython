import requests
import pandas as pd

limit = 30
skip = 0
listpd = []

while True:
    url = f'https://dummyjson.com/users?limit={limit}&skip={skip}'
    response = requests.get(url)
    data = response.json()['users']

    listpd.append(pd.DataFrame(data))

    total = response.json()['total']
    skip += limit

    if skip >= total:
        break

users = pd.concat(listpd, ignore_index=True)

print(users.head())

users.to_csv('users.csv', index=False)
print("Saved to users.csv")