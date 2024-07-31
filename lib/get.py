import requests #coming from Request class.
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url) # get() dict method.

json_content = json.loads(response.text)  # Deserialize/decode data as JSON, turns JSON data into list.

print(json.dumps(json_content, indent=4)) # dumps()  encode/serialize data as JSON.


#json -- JSON encoder and decoder.
#indent=4 => pretty printing: 

# {
#     "4": 5,
#     "6": 7
# }

