import requests as req
from pprint import pprint
import os

username = os.environ["SNOW_USER"]
password = os.environ["SNOW_PASSWORD"]
instance = os.environ["SNOW_INST"]

uri = "https://"+instance+".service-now.com/api/now/table/incident"
response = req.get(uri, auth=(username, password))
pprint(response.text)