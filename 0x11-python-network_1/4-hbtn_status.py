#!/usr/bin/python3
"""this is a simple program getting informations of a connection using requestes.
"""

import requests

if __name__ == "__main__":
    request =  requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(request.text))
    print("\t- content:", request.text)
