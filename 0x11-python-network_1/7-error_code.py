#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided,
using the web server running on port 5000
"""

import requests
from sys import argv

if __name__ == '__main__':
    target_url: str = argv[1]

    response = requests.get(target_url)
    status_code: int = response.status_code
    response_body = response.text

    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(response_body)
