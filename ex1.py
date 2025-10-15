import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)


if response.status_code == 200:
  
    users = response.json()
    
    
    for user in users:
        print(f"Nome: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Endereço: {user['address']['street']}, {user['address']['city']}")
        print("-" * 40)
else:
    print(f"Erro ao acessar a API. Status code: {response.status_code}")