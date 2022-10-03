import requests
import random
import json

#Get the data from the API
response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()
json_string = json.dumps(data)
parsed_json = json.loads(json_string)

#Get the names from the API
fnames = []
lnames = []
for i in range(10):
    fnames.append(parsed_json["results"][i]["name"]["first"])
    lnames.append(parsed_json["results"][i]["name"]["last"])

#Get a random name from the list
random_fname = random.choice(fnames)
random_lname = random.choice(lnames)

#Show the name to the user
print("Your random name is: " + random_fname + " " + random_lname)


