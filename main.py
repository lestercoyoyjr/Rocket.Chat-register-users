import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Rocket.Chat API endpoint for creating a user
base_url= os.getenv("URL")
url = base_url + "/api/v1/users.create"

# Headers with authentication tokens
headers = {
    "X-Auth-Token": os.getenv("X-Auth-Token"),
    "X-User-Id": os.getenv("X-User-Id"),
    "Content-Type": "application/json",
}


# Number of users to create
while True:
    try:
        base_number = int(input("Enter the starting number (e.g., 1): "))
        num_users = int(input("Enter the number of users: "))
        break  # Break out of the loop if both inputs are valid integers
    except ValueError:
        print("Please enter valid integer values for both the starting number and the number of users. Try again.\n\n")

# Now you can use base_number and num_users in your code
print("Starting number:", base_number)
print("Number of users:", num_users)


for i in range(base_number, base_number + num_users):
    user_data = {
        "name": "test-user" + str(i),
        "username": "test.user" + str(i),
        "email": "test.user" + str(i) + "@gmail.com",
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