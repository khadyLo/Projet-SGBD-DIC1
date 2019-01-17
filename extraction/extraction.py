#importation de la classe elementTree(ET)  pour enrouler un element de structure afin de le convertir en xml
import xml.etree.ElementTree as ET

def extraction_data_json(data):
    dictEntity = {}
    dictAssoc = {}

    for entity in data['entities']:
        liste_attr = []
        for attr in data['entities'][entity]['attributs']:
            liste_attr.append(attr)
        dictEntity[entity] = liste_attr

    for assoc in data['associations']:
        liste_assoc = []
        for ass in data['associations'][assoc]:
            liste_assoc.append(data['associations'][assoc][ass])
            liste_assoc.append(ass)
        dictAssoc[assoc] = liste_assoc

    return dictEntity, dictAssoc

#definition d'une fonction appelee extraction_data_xml prenant en parametre root, la balise racine
def extraction_data_xml(root):

    
    #definition de dictionnaires vides: entites et associations
    dictEntity = {}
    dictAssoc = {}
    
   #parcours du fichier afin d'en extraire l'ensemble des entites(LISTE)
    for entities in root.findall('entities'):

        #parcours du fichier pour recuperer les entites une a une
        for entity in entities.findall('entity'):

             #definition d'une liste vide
            liste = []

            #detection, recuperation et stockage des noms d'entites dans une variable name_entity 
            name_entity = entity.find('name').text

            #parcours du fichier pour extraire la liste des attributs stockee dans la variable tag_attr
            for attr in entity.findall('attributs'):
                tag_attr = attr.findall('attribut')

                #parcours de la liste des attributs afin de les extraire un a un
                for i in tag_attr:
                    name_attr = i.text

                     #on ajoute a la liste predefinie chacun des attributs
                    liste.append(name_attr)

             #la liste est ensuite placee dans le dictionnaire predefini       
            dictEntity[name_entity] = liste

    #parcours du fichier afin d'en extraire l'ensemble des associations(LISTE)
    for assoc in root.findall('associations'):

        #parcours du fichier pour recuperer les associations une a une
        for ass in assoc.findall('association'):

            #definition d'une liste vide
            liste_assoc = []

           #verification de la presence d'une chaine de caractere placee ensuite dans la variable name_assoc(cas association)
            name_assoc = ass.find('name_assoc').text

            #definition de la plage(debut et fin) dans laquelle , la verification devra se faire, on place le resultat dans les variables card_deb et card_fin(cas entite) 
            name_entity_deb = ass.find('entityDeb').text
            card_deb = ass.find('cardDeb').text
            name_entity_fin = ass.find('entityFin').text
            card_fin = ass.find('cardFin').text

            #on ajoute a la liste predefinie les valeurs precedentes
            liste_assoc.append(card_deb)
            liste_assoc.append(name_entity_deb)
            liste_assoc.append(card_fin)
            liste_assoc.append(name_entity_fin)

            #la liste est ensuite placee dans le dictionnaire predefini    
            dictAssoc[name_assoc] = liste_assoc
            
    return dictEntity, dictAssoc
