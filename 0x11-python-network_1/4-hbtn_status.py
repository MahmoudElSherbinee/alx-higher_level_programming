#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example
(tabulation before -)
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    my_request = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(my_request.text)))
    print("\t- content: {}".format(my_request.text))
