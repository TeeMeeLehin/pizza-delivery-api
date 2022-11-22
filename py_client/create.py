from email import header
import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/auth/jwt/create/"

email = input("What is your email?\n")
password = getpass("Enter your password.\n")

auth_response = requests.post(auth_endpoint, json= {"email":email, "password":password})
print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()['access']
    headers= {
        "Authorization":f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/orders/"
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())

print(auth_response.status_code)


