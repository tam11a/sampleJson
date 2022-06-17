import json
from glob import glob

template_x = {
        "dataset_name": "",
        "image_link": "",
        "annotation_type": "image",
        "annotation_objects": {
            "vehicle": {
                "presence": 0,
                "bbox": []
            },
            "license_plate": {
                "presence": 0,
                "bbox": []
            }
        },
        "annotation_attributes": {
            "vehicle": {
                "Type": None,
                "Pose": None,
                "Model": None,
                "Make": None,
                "Color": None
            },
            "license_plate": {
                "Difficulty Score": None,
                "Value": None,
                "Occlusion": None
            }
        }
    }


for file_name in glob('jsons/*.png.json'):
    output = []
    template = template_x
    # Opening JSON file
    f = open(file_name)

    # returns JSON object as 
    # a dictionary
    data = json.loads(f.read())
    # Iterating through the json
    f.close()

    template['dataset_name'] = file_name.split('/')[-1]

    for i in data['objects']:
        if i['classTitle'].lower() == 'vehicle':
            template['annotation_objects']['vehicle']['presence'] = 1
            for j in i['points']['exterior']:
                template['annotation_objects']['vehicle']['bbox'].extend(j)
            for j in i['points']['interior']:
                template['annotation_objects']['vehicle']['bbox'].extend(j)
            for j in i['tags']:
                template['annotation_attributes']['vehicle'][j['name']] = j['value']

        elif i['classTitle'].lower() == 'license plate':
            template['annotation_objects']['license_plate']['presence'] = 1
            for j in i['points']['exterior']:
                template['annotation_objects']['license_plate']['bbox'].extend(j)
            for j in i['points']['interior']:
                template['annotation_objects']['license_plate']['bbox'].extend(j)
            for j in i['tags']:
                template['annotation_attributes']['license_plate'][j['name']] = j['value']
    output.append(template)
    with open('formatted/formatted_'+file_name.split('/')[-1], 'w') as f:
        json.dump(output, f)