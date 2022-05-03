import re
import requests
from requests.structures import CaseInsensitiveDict




data = """
{
  "name": fefe,
  "passw": 123,
}
"""

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = requests.post("http://127.0.0.1:8000/room/LoginViewSet/confirm", data=data, headers=headers)

print(data)
