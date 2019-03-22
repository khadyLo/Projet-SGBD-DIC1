# coding=utf-8

import xml.etree.ElementTree as ET

def extraction_data_xml(root):
    dictEntity = {}
    dictAssoc = {}

    for entities in root.findall('entities'):
        for entity in entities.findall('entity'):
            liste = []
            name_entity = entity.find('name').text
            for attr in entity.findall('attributs'):
                tag_attr = attr.findall('attribut')
                for i in tag_attr:
                    name_attr = i.text
                    liste.append(name_attr)
            dictEntity[name_entity] = liste

    for assoc in root.findall('associations'):
        for ass in assoc.findall('association'):
            liste_assoc = []
            name_assoc = ass.find('name_assoc').text
            name_entity_deb = ass.find('entityDeb').text
            card_deb = ass.find('cardDeb').text
            name_entity_fin = ass.find('entityFin').text
            card_fin = ass.find('cardFin').text
            liste_assoc.append(card_deb)
            liste_assoc.append(name_entity_deb)
            liste_assoc.append(card_fin)
            liste_assoc.append(name_entity_fin)
            dictAssoc[name_assoc] = liste_assoc
            
    return dictEntity, dictAssoc