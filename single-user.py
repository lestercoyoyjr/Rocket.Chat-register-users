import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Rocket.Chat API endpoint for creating a user
url = "http://localhost:3000/api/v1/users.create"

# Headers with authentication tokens
headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}

# User data to create
user_data = {
    "name": "test-agent11",
    "username": "test.agent11",
    "email": "test.agent11@gmail.com",
    "password": "1234",
    "active" : True,
    "roles":["user"]        
}

try:
    # Send POST request to create the user
    response = requests.post(url, headers=headers, json=user_data)

    # Check the response status code
    if response.status_code == 200:
        print("User created successfully!")
    else:
        print(f"Failed to create user. Status code: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"An error occurred: {str(e)}")
