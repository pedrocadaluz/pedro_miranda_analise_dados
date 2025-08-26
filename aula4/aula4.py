import requests
import pandas as pd

uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'fdb570a7282c4dceac2fbb71a7104c05' }
response = requests.get(uri, headers=headers)
response = response.json()
matches = response["matches"]
df= pd.DataFrame(matches)