import re
import unicodedata
def normalize(s):
	return unicodedata.normalize("NFKD", s.casefold())
def equalsIgnoreCase(left, right):
	if left==None:
		return False
	if right==None:
		return False
	return normalize(left) == normalize(right)
def getLines(inputText):
    #this workks for pure english
    #pat = re.compile(r".*[a-z]+.*\n")
    pat = re.compile(r".*\n")
    matches = pat.findall(inputText)
    return matches
def loadList(fileName,lowerCase=False):
    f = open(fileName, encoding='utf-8-sig')
    text = f.read()
    if lowerCase:
        text = text.lower()
    f.close()
    lines = getLines(text)
    stringList = []
    for line in lines:
        stringList.append(line.rstrip("\r\n"))
    #print('file:',fileName)
    return stringList
def replaceExtrasWithSpace(name,extras):
    for e in extras:
        name = name.replace(e,' ')
    return name