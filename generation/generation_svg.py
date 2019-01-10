import os
def generate_svg(outputfile, dict):
    output = open(outputfile, "a")
    for entity in dict:
        output.write(entity.upper() + ": ")
        for attr in dict[entity]:
            output.write(attr + ", ")
        output.write("\n")
    if os.stat(outputfile).st_size != 0:
        os.system("mocodo --input " + outputfile)