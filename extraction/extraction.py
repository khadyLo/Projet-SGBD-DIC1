
def extraction_data_json(data):
    dict = {}

    for entity in data:
        liste_attr = []
        for attr in data[entity]['attributs']:
            liste_attr.append(attr)
        dict[entity] = liste_attr

    return dict
