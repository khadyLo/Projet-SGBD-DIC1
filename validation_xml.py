import xml.etree.ElementTree as ET
import requests


def load_xml_local_file(file):
    try:
        tree = ET.parse(file)
        return tree
    except ET.ParseError as error:
        print("fichier xml invalide: %s" % error)


def load_xml_remote_file(url):
    try:
        ''' response = requests.get(url) '''
        tree = ET.parse(url)
        return tree
    except requests.exceptions.HTTPError as error1:
        print("Erreur HTTP: %s" % error1)
    except ET.ParseError as error:
        print("fichier xml invalide: %s" % error)
