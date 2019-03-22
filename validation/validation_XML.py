#importation des modules installes
import xml.etree.ElementTree as ET
import requests

#definition d'une fonction prenant en parametre un fichier xml
def load_xml_local_file(file):

    #verification de la validite du fichier(s'il peut etre parse en xml) par recuperation
    try:
        tree = ET.parse(file)
        return tree

    #s'il ne peut etre parse, on indique que le fichier est invalide
    except ET.ParseError as error:
        print("fichier xml invalide: %s" % error)


#definition d'une fonction prenant en parametre un url et test de sa validite
def load_xml_remote_file(url):

    #recuperation du fichier a partir de l'url et verification de la validite
    try:
        response = requests.get(url)
        tree = ET.parse(response.text)
        return tree
    except requests.exceptions.HTTPError as error1:
        print("Erreur HTTP: %s" % error1)
    except ET.ParseError as error:
        print("fichier xml invalide: %s" % error)
