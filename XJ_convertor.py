# coding=utf-8

# Importation des modules
import getopt
import os
import sys
import requests
import xml.etree.ElementTree as ET
import urllib

# Importation des modules créés
from cmd_config import cmd
from validation import validation_json, validation_xml
from extraction import extraction_json, extraction_xml
from generation import generation_svg


def XJ_convertor(argv):
    # Variables globales
    urlFluxHTTP = ''
    inputFile = ''
    outputFile = ''
    fileType = ''
    outputScan = False
    data_JSON = ''
    data_XML = ''
    dictEntity = {}
    dictAssoc = {}

    # Recupération des options et arguments de la commande entrée 
    try:
        opts, args = getopt.getopt(argv, "ai:th:f:o:", [
                                   "i_xml/json=", "h_urlFluxHTTP=", "f_FichierInput=", "o_nomFichierSvg="])
    except getopt.GetoptError:
        print(
            'XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg : n°1')
        sys.exit(2)

    # Vérification de la validation de la commande entrée
    for opt, arg in opts:
        if opt == '-a':
            print(
                'XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg : n°2')
            sys.exit()
        elif opt in ("-i", "--i_xml/json"):
            fileType = arg
        elif opt == '-t':
            outputScan = True
        elif opt in ("-h", "--h_urlFluxHTTP"):
            urlFluxHTTP = arg
        elif opt in ("-f", "--f_FichierInput"):
            inputFile = arg
        elif opt in ("-o", "--o_nomFichierSvg"):
            outputFile = arg
        else:
            print('La commande est invalide')

    # Validation de la commande par True ou False
    check_command = cmd.validation_cmd(fileType, urlFluxHTTP, inputFile, outputFile)

    # Si la commande est valide
    if check_command == True:
        # Si le type de fichier est json
        if fileType == 'json':
            # Vérification du provenance du fichier (Local ou distant)
            if cmd.url_or_local(urlFluxHTTP, inputFile) == 'local':
                # Recupération du contenu du fichier
                data_JSON = validation_json.load_json_local_file(inputFile)
            elif cmd.url_or_local(urlFluxHTTP, inputFile) == 'url':
                # Recupération du contenu du fichier
                data_JSON = validation_json.load_json_remote_file(urlFluxHTTP)
            
            # Extraction des entités et des relations enregistrées dans des dictionnaires
            dictEntity, dictAssoc = extraction_json.extraction_data_json(data_JSON)
            # Affichage du modèle en présence de l'option -t 
            if outputScan == True:
                print("Affichage des entités et associations")
                print("=======================================")
                print(dictEntity)
                print(dictAssoc)
                print("=======================================")
                print("\n\n\n")
            # génération du fichier .svg à partir des dictionnaires des entités et des associations
            file = generation_svg.generate_mcd(outputFile, dictEntity, dictAssoc)
            generation_svg.generate_svg_json(file)

        # Si le type de fichier est xml
        if fileType == 'xml':
            # Vérification du provenance du fichier (Local ou distant)
            if cmd.url_or_local(urlFluxHTTP, inputFile) == 'local':
                # Recupération du contenu du fichier
                tree = ET.parse(inputFile)
                root = tree.getroot()
            elif cmd.url_or_local(urlFluxHTTP, inputFile) == 'url':
                ''' response = requests.get(urlFluxHTTP) '''
                # Recupération du contenu du fichier
                tree = ET.parse(urllib.request.urlopen(urlFluxHTTP)) 
                root = tree.getroot()
            # Extraction des entités et des relations enregistrées dans des dictionnaires
            dictEntity, dictAssoc = extraction_xml.extraction_data_xml(root)
            # Affichage du modèle en présence de l'option -t
            if outputScan == True:
                print("Affichage des entités et associations")
                print("=======================================")
                print(dictEntity)
                print(dictAssoc)
                print("=======================================")
                print("\n\n\n")
            # génération du fichier .svg à partir des dictionnaires des entités et des associations
            file = generation_svg.generate_mcd(outputFile, dictEntity, dictAssoc)
            generation_svg.generate_svg_xml(file)


if __name__ == '__main__':
    XJ_convertor(sys.argv[1:])