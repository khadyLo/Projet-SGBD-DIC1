
import json 


from pprint import pprint 
with open('../classes.json') as f: 
    data = json.load(f)

pprint(data)

def json_validator(f):
    try:
        json.loads(f)  
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

print(json_validator('../classes.json')) 

