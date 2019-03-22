# coding=utf-8

import xml.etree.ElementTree as ET

#Definition de la fonction extraction_data_json prenant en parametre (data)
def extraction_data_json(data):
 #Definition des dictionnaires vides
    dictEntity = {}
    dictAssoc = {}
#Parcours  pour extraire les entit�s
    for entity in data['entities']:
#Definition d'une liste vide
        liste_attr = []
#Parcours  pour extraire les attributs 
        for attr in data['entities'][entity]['attributs']:
#Ajout d'un attribut dans la liste (liste_attr)
            liste_attr.append(attr)
#Ajout de la liste des attributs dans le dictionnaire index� par le nom 'entity'
        dictEntity[entity] = liste_attr
#Parcours  pour extraire les associations
    for assoc in data['associations']:
#Definition d'une liste vide
        liste_assoc = []
#Parcours pour extraire les associations
        for ass in data['associations'][assoc]:
#Ajout des association dans la liste (liste_assoc)
            liste_assoc.append(data['associations'][assoc][ass])
            liste_assoc.append(ass)
#Ajout de la liste des associations dans le dictionnaire index� par le nom 'assoc'
        dictAssoc[assoc] = liste_assoc

    return dictEntity, dictAssoc