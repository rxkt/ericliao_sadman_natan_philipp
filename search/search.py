import google
import nameFind

def getPages(query):
	results=google.search(query, start=1,  stop=10, pause=0.1)
	urls = []
	for url in results:
		urls.append(url)
	return urls

def getNames(urls):
	final = {}
	for url in urls:
		names = nameFind.nameList(google.get_page(url))
		final = nameFind.addDicts(final,names)
	return final

if __name__ == "main":
    pages=getPages("Who played Spiderman?")
    names=getNames(pages)
    prcnt=nameFind.percentDict(names)
    print nameFind.mostCommon(prcnt)
