import requests

state = 'Maharashtra'.lower()
city = 'Mumbai'.lower()
api_address = "https://api.covid19india.org/state_district_wise.json"
json_data = requests.get(api_address).json()
num=range(1,39)

for n in num:
    for state in num:
        if (city == json_data[state].lower()):
            formatted_json = json_data['state']['districtData'][n]['active']
    state+=1
    n+=1
print(f"Active Case in {state} is {formatted_json}")