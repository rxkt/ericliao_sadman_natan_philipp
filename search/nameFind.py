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
    fTitles = re.findall("(Mr|Mrs|Miss|Ms|Hon|Dr|Sir|Hon|Fr|Esq|King)(\.)?\s{0,1}([A-Z][A-Za-z'\-]*)?([ ][A-Z][A-Za-z'\-]*)?", content)
    
    titles = []
    for word in fTitles:
        fin = ""
        """if word[1] == '':
word[1] = ' '"""
        for part in word:
            fin += part
        titles.append(fin)
 
    firstPass.extend(titles)
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
        
    keys=names.keys()
    vals=names.values()

    #print keys
    #print vals

    names={v:k for k,v in names.items()}
    print names
    

nameList(test)
