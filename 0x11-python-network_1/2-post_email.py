#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

The email must be sent in the email variable
You must use the packages urllib and sys
You are not allowed to import packages other than urllib and sys
You don't need to check arguments passed to the script (number or type)
You must use the with statement
Please test your script in the sandbox provided,
using the web server running on port 5000
    """

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urlencode({"email": email}).encode("utf-8")
    my_request = Request(url, data=data)

    with urlopen(my_request) as response:
        body = response.read()

    print(body.decode("utf-8"))
