import xml.etree.ElementTree as ET

def extraction_data_xml(root):
    dict = {}

    for entities in root.findall('entities'):
        for entity in entities.findall('entity'):
            liste = []
            name_entity = entity.find('name').text
            for attr in entity.findall('attributs'):
                tag_attr = attr.findall('attribut')
                for i in tag_attr:
                    name_attr = i.text
                    liste.append(name_attr)
            dict[name_entity] = liste
            
    return dict