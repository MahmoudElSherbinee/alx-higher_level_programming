#!/usr/bin/python3

"""Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token
as password to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password
(in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)
"""

import requests
from sys import argv

if __name__ == "__main__":
    username_input: str = argv[1]
    access_token_input: str = argv[2]

    api_endpoint: str = "https://api.github.com/user"

    response = requests.get(api_endpoint,
                            auth=(username_input, access_token_input))
    response_status: int = response.status_code

    if response_status == 200:
        user_id = response.json().get("id")
        print(f"User ID: {user_id}")
    else:
        print(f"Failed to retrieve user ID. Status code: {response_status}")
