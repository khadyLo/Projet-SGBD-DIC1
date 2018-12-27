# importation du bibliotheque json
import json 
def json_validator(data):
    try:
        json.loads(data)   # la fonction jason.loads() permet de faire la validation du fichier json
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False
""" 
#Valid JSON Data
{
  "classes":[ 
    {"id":"1","nom":"DIC1", "departement":"DGI"},
    {"id":"2","nom":"DIC2", "departement":"DGI"}
    ]
}
#Invalid JSON Data
 {
  "classe":[ 
    {"id":"1","nom":"DIC1", "departement":"DGI"},
    {"id":"2","nom":"DIC2", "departement":"DGI"}
    ]
}
 """
print(json_validator('{"classes":[{"id":"1","nom":"DIC1","departement":"DGI"},{"id":"2","nom":"DIC2","departement":"DGI"}]}' ))#prints True
print (json_validator('{"classe":[{"id":"1","nom":"DIC1","departement":"DGI"},{"id":"2","nom":"DIC2","departement":"DGI"}]}')) #prints Error message and False
