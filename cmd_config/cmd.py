# coding=utf-8

import sys
import getopt


def validation_cmd(fileType, urlFluxHTTP, inputFile, outputFile):
    if fileType != 'xml' and fileType != 'json':
        print(
            "La commande doit être de ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()
    if (urlFluxHTTP == '' and inputFile == '') or (urlFluxHTTP != '' and inputFile != ''):
        print(
            "La commande doit être de ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()
    if outputFile == '':
        print(
            "La commande doit être de ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()
    return True

def url_or_local(urlFluxHTTP, inputFile):
    if urlFluxHTTP == '' and inputFile != '':
        return 'local'
    elif urlFluxHTTP != '' and inputFile == '':
        return 'url'
