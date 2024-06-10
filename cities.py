import pandas as pd
import json
from unidecode import unidecode

database = pd.read_csv('worldcities.csv')
print(database.head())
print(database.columns)
database_romania = database[database['country'] == 'Romania']
romanian_countys = {}
for index,row in database_romania.iterrows():
    county = unidecode(row['admin_name'])
    if county in romanian_countys:
        romanian_countys[county].append(unidecode(row['city']))
    else:
        romanian_countys[county] = [unidecode(row['city'])]

with open('cities.json','w') as f:
    json.dump(romanian_countys,f)