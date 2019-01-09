# importation du bibliotheque json
import json 

def json_validator(data):
    try:
        json.loads(data)  # la fonction json.loads() permet de faire la validation du fichier json
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

print(json_validator("../classes.json")) #print True
