import re

fi = open("test/nick.txt","r")
test = fi.read()
fi.close()

def nameList(content):
    
    #Start at 16484
    fi2 = open("/usr/share/dict/words", "r")
    dictionary = fi2.read()
    words=dictionary.split("\n")
    words=words[16484:]
    fi2.close()
    
    for i in range(len(words)):
        words[i]=words[i].upper()

    firstPass = re.findall("[A-Z][A-Za-z'\-]*\s[A-Z][A-Za-z'\-]*", content)

    secondPass = []
    for word in firstPass:
        if "--" in word:
            names=re.findall("[\w]+",word)
        else:
            names=word.split(" ")
        check=True
        for name in names:
            if name.upper() in words or len(name)<4:
                check=False
        if check:
            secondPass.append(word)

    names={}
            
    for word in secondPass:
        if word not in names:
            names[word]=0
        names[word] = names[word]+1

    totalNames=0
        
    for name in names:
        totalNames = totalNames + names[name]
        
    return names
    
def addDicts (dict1, dict2):
	dict3 = {}
	for name in dict1.keys():
		dict3[name] = dict1[name]
	for name in dict2.keys():
		if name in dict3.keys():
			dict3[name] = dict3[name]+dict2[name]
		else:
			dict3[name] = dict2[name]
	return dict3

def percentDict(names):
	total = 0.0
	for name in names:
		total = total + names[name]
	for name in names:
		names[name] = names[name]/total
	names={v:k for k,v in names.items()}
	return names

def mostCommon(names):
	highest=0.0
	name=""
	for percent in names:
		if percent>highest:
			highest=percent
			name=names[percent]
	return {name:highest}

perc=percentDict(nameList(test))
print mostCommon(perc)
