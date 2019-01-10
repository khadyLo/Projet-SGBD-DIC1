import getopt
import sys
import xml.etree.ElementTree as ET


from cmd_config import cmd
from validation import validation_json, validation_xml
from extraction import extraction
from generation import generation_svg


def XJ_convertor(argv):
    urlFluxHTTP = ''
    inputFile = ''
    outputFile = ''
    fileType = ''
    outputScan = False
    data_JSON = ''
    data_XML = ''
    dict = {}

    try:
        opts, args = getopt.getopt(argv, "ai:th:f:o:", [
                                   "i_xml/json=", "h_urlFluxHTTP=", "f_FichierInput=", "o_nomFichierSvg="])
    except getopt.GetoptError:
        print(
            'XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg : n°1')
        sys.exit(2)

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

    check_command = cmd.validation_cmd(fileType, urlFluxHTTP, inputFile, outputFile)
    print(check_command)

    if check_command == True:
        if fileType == 'json':
            if cmd.url_or_local(urlFluxHTTP, inputFile) == 'local':
                data_JSON = validation_json.load_json_local_file(inputFile)
            elif cmd.url_or_local(urlFluxHTTP, inputFile) == 'url':
                data_JSON = validation_json.load_json_remote_file(urlFluxHTTP)
            
            dict = extraction.extraction_data_json(data_JSON)
            generation_svg.generate_svg(outputFile, dict)


if __name__ == '__main__':
    XJ_convertor(sys.argv[1:])