import re
import requests


data = requests.post("http://127.0.0.1:8000/room/login/confirm")

print(data)
