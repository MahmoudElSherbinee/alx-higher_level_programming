#!/usr/bin/python3

"""
This Python code snippet sends an HTTP GET request
to "https://alx-intranet.hbtn.io/status" using the urllib.request module.
It then prints information about the response, including its type,
raw bytes content, and decoded UTF-8 content.
The script is designed to execute only when run directly as a script.
"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    my_request = Request(url)

    with urlopen(my_request) as response:
        the_result = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(the_result)))
    print("\t- content: {}".format(the_result))
    print("\t- utf8 content: {}".format(the_result.decode("utf-8")))
