import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Rocket.Chat API endpoint for creating a user
url = "https://lestercch.rocket.chat/api/v1/users.create"

# Headers with authentication tokens
headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}


# User data to create a single user account
user_data = {
    "name": "test-agent18",
    "username": "test.agent18",
    "email": "test.agent18@gmail.com",
    "password": "1234",
}

"""
User data to create several accounts

# Define the number of users you want to create
num_users = 2  # Change this number to the desired number of users

for i in range(17, num_users + 1):
    user_data = {
        "name": "test-agent" + str(i),
        "username": "test.agent" + str(i),
        "email": "test.agent" + str(i) + "@gmail.com",
        "password": "1234",
    }

# You can also use the try-catch but don't forget about not avoiding loop
"""

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