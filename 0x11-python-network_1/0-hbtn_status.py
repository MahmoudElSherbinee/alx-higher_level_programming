#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
#
# You must use the package urllib
# You are not allowed to import any packages other than urllib
# The body of the response must be displayed
# like the following example (tabulation before -)
# You must use a with statement

import urllib.request

if __name__ == "__main__":
    my_request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(my_request) as response:
        the_result = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_result)))
        print("\t- content: {}".format(the_result))
        print("\t- utf8 content: {}".format(the_result.decode("UTF-8")))
