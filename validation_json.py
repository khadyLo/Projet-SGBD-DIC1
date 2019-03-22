#Importation des modules json et request
import json
import requests

#Definition d'une fonction prenant en parametre un fichier
def load_json_local_file(file):
    try:
#Ouverture du fichier en mode lecture dans une variable 
        with open(file, "r") as f:
#Chargement du contenu d'une variable(f) dans une variable(data)
            data = json.load(f)
#Data en retour
        return data
    except ValueError as error:
        print("fichier json invalide: %s" % error)

#Definition d'une fonction prenant en parametre l'url
def load_json_remote_file(url):
    try:
        print(url)
#Recuperation du fichier se trouvant dans l'url et stockage dans le variable(response) 
        response = requests.get(url)
#Chargement du contenu (response.text) dans une variable (data)
        data = json.loads(response.text)
        return data
#Data en retour
    except requests.exceptions.HTTPError as error1:
#erreur de l'url
        print("Erreur HTTP: %s" % error1)
    except ValueError as error2:
#erreur du fichier du fichier.text
        print("fichier json invalide: %s" % error2)
