import json
from glob import glob

output = []
for jsonFile in glob('jsons/*.png.json'):
    # Opening JSON file
    f = open(jsonFile)
    
    # returns JSON object as 
    # a dictionary
    data = json.loads(f.read())
    # Iterating through the json
    # list
    for i in data['objects']:
        if i['classTitle'].lower() == 'vehicle':
            i['classTitle'] = 'Car'
        elif i['classTitle'].lower() == 'license plate':
            i['classTitle'] = 'Number'
        
    output.append(data)
    # Closing file
    f.close()   

with open('formatted/problem2.json', 'w') as f:
	json.dump(output, f)