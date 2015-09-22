from templateApply import getAll
from htmlOrTxtToJsonParser import parse, navigationParse

#parse()
#getAll()

k="MFA"
file = open("./navigations/"+k+".txt", "r")
navigationJson = navigationParse(file)
file.close()
file = open("./navigationJson/"+k+".json", "w", encoding= "utf8")
file.writelines(navigationJson)
file.close()