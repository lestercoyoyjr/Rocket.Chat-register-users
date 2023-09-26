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


# Number of users to create
base_number = 1 # the number where the count will start
num_users = 4  # Change this to the desired number of users

for i in range(base_number, base_number + num_users):
    user_data = {
        "name": "test-agent" + str(i),
        "username": "test.agent" + str(i),
        "email": "test.agent" + str(i) + "@gmail.com",
        "password": "1234",
        "active" : True,
        "roles":["user"]        
    }

    try:
        # Send POST request to create the user
        response = requests.post(url, headers=headers, json=user_data)

        # Check the response status code
        if response.status_code == 200:
            print(f"User test.agent-{i} created successfully!")
        else:
            print(f"Failed to create user test.agent{i}. Status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"An error occurred while creating user {i}: {str(e)}")