#importation des modules
import sys
import getopt

#definition d'une fonction pour la validation de commande avec en parametres les differents arguments: type de fichier avec un input et un output
def validation_cmd(fileType, urlFluxHTTP, inputFile, outputFile):

    #specification des valeurs pour le format: soite xml ou json et indication du format recherche si le type renseigne est different de ceux-la
    if fileType != 'xml' and fileType != 'json':
        print(
            "La commande doit être sous ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()

    #specification d'un input en flux http   
    if (urlFluxHTTP == '' and inputFile == '') or (urlFluxHTTP != '' and inputFile != ''):
        print(
            "La commande doit être sous ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()

    
    #specification d'un output en flux http    
    if outputFile == '':
        print(
            "La commande doit être sous ce format : \n \tXJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg")
        sys.exit()
    return True

#definition d'une fonction indiquant si le fichier est en local ou correspond a un url
def url_or_local(urlFluxHTTP, inputFile):

    #si l'url est vide et l'input non vide on retourne la valeur locale(on a un fichier local) 
    if urlFluxHTTP == '' and inputFile != '':
        return 'local'
    
    #sinon on renvoie url
    elif urlFluxHTTP != '' and inputFile == '':
        return 'url'
