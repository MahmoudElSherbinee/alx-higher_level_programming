#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don't need to error check arguments passed to the script (number or type)
Please test your script in the sandbox provided,
using the web server running on port 5000
"""

import requests
from sys import argv

if __name__ == "__main__":
    target_url: str = argv[1]
    user_email: str = argv[2]
    payload_data: dict = {"email": user_email}

    response = requests.post(target_url, data=payload_data)
    response_body = response.text

    print(response_body)
