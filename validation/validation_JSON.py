import json
import requests


def load_json_local_file(file):
    try:
        with open(file, "r") as f:
            data = json.load(f)
        return data
    except ValueError as error:
        print("fichier json invalide: %s" % error)


def load_json_remote_file(url):
    try:
        response = requests.get(url)
        data = json.load(response.text)
        return data
    except requests.exceptions.HTTPError as error1:
        print("Erreur HTTP: %s" % error1)
    except ValueError as error2:
        print("fichier json invalide: %s" % error2)
