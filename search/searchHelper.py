import re
import wikipedia

#fi = open("test/nick.txt","r")
#test = fi.read()
#fi.close()

def extractNames(content):
    # Start dctionary at 16484
    fi2 = open("/usr/share/dict/words", "r")
    dictionary = fi2.read()
    words=dictionary.split("\n")
    words=words[16484:]
    fi2.close()
    
    # Uppercase words
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

def extractDates(content):
	firstPass = re.findall("(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|(Sep|Nov|Dec)(ember)?|Oct(ober)) [0-9]{0,4}(st|nd|rd|th)?,?( [0-9]{0,4})?", content)
	dates={}
	for word in firstPass:
		if word not in dates:
			dates[word[0]+word[-1]]=0
		dates[word[0]+word[-1]] = dates[word[0]+word[-1]]+1

	return dates


# These are the results from one page. We're artificially changing the frequency.
# Say we have five pages, and gradient = 0.1. Their results will be weighted like this:
# #1 1.2
# #2 1.1
# #3 1.0
# #4 0.9
# #5 0.8
def weightNames(namesByFrequency, index, total):
    gradient = 0.1

    # For every name in ths page, apply the formula below to compute weighted value
    for name in namesByFrequency:
        namesByFrequency[name] *= -gradient * index + 1.0 + ((total + 1) / 2 * gradient)

    # Formula explained:
    # It's an arithmetic series. Every time index increases by 1, the weight decreases by gradient.
    # To that we add some fixed value such that the middle index always = 1.0 and the highest and lowest are correct.
    # That fixed value is 1.0 + ((total + 1) / 2 * gradient)
    # If we have 5 indices total, we add 1 and divide by 2 to get 3.
    # We multiply 3 by gradient (0.1) to get 0.3.
    # We add 1.0 to get 1.3. This is the weight at index = 1. At higher indices it decreases.

    return namesByFrequency

def fetchBiography(name):
    name = " ".join(name)
    print "Fetching bio for " + name
    if "ALEX TREBEK" in name:
        return "Who is Alex Trebek?"

    try:
        return wikipedia.summary(name, sentences = 2)
    except wikipedia.exceptions.DisambiguationError:
        return False
    
def addDicts (dict1, dict2):
	dict3 = {}
	for name in dict1.keys():
		dict3[name] = dict1[name]
	for name in dict2.keys():
		if name in dict3.keys():
			dict3[name] = dict3[name] + dict2[name]
		else:
			dict3[name] = dict2[name]
	return dict3

def compareNames(names):
	total = 0.0
	for name in names:
		total += names[name]

	for name in names:
		names[name] = names[name] / total

	names={percent:name for name, percent in names.items()}

	return names

# Returns tuple (name, percent) of most common name
# Note that this is more logical than a dict, so I changed it.
def mostCommon(names):
	highest=0.0
	name = ""
	for percent in names:
		if percent > highest:
			highest = percent
			name = names[percent]
	return name

