import json
import sys
with open("../classes.json") as f:
	data_JSON = json.load(f)
dict = {}
for cle in data_JSON:
	liste = []
	for attr in data_JSON[cle]['attributs']:
		liste.append(attr)
	dict[cle] = liste
print(dict)
'''fileOutput = open("", "a")'''

"""for entity in dict:
	fileOutput.write(entity.upper() + ": ")
	for attr in dict[entity]:
		fileOutput.write(attr + ", ")
	fileOutput.write("\n")"""