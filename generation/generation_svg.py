#Importation du module os
import os
#Definition d'une fonction prenant en parametre le fichier de sortie,les dictionnaires (entity et assoc)
def generate_mcd(outputfile, dictEntity, dictAssoc):
    # Recupération du nom fichier de sortie et création du fichier .mcd
    out = outputfile.replace(".svg", ".mcd")
    # Ouverture du fjchier en écriture
    output = open(out, "w")

    # Parcours du dictionnaire des entités et écriture dans le fichier .mcd
    for assoc in dictAssoc:
        output.writelines(assoc + ", ")
        for idx, conn in enumerate(dictAssoc[assoc]):
            output.write(conn + " ")
            if idx == 1:
                output.write(", ")
        output.write("\n")
    # Parcours du dictionnaire des associations et écriture dans le fichier .mcd
    for entity in dictEntity:
        output.writelines(entity + ": ")
        for attr in dictEntity[entity]:
            output.write(attr + ", ")
        output.write("\n")

    # Return le fichier .mcd
    return out

# génération du fichier .svg grâce au module mocodo
def generate_svg(file):
    os.system("mocodo --input " + file)
