import google
import searchHelper
from cookielib import CookieJar

# Odd number to make weighting easier
NUM_GOOGLE_RESULTS = 3

# Main function
def query(searchStr):
    pages = getPages(searchStr)

    # "Who played Chase" becomes ["WHO", "PLAYED", "CHASE"]
    wordsInQuery = [word.upper() for word in searchStr.split(" ")]
    if len(wordsInQuery) >= 3:
        if wordsInQuery[0] + wordsInQuery[1] == "WHOIS" or wordsInQuery[0] + wordsInQuery[1] == "WHOWAS":
            biography = searchHelper.fetchBiography(wordsInQuery[2:])
            if biography:
                return biography

    names = parsePages(pages, wordsInQuery)
    return searchHelper.mostCommon(names)

# Searches Google for query
def getPages(query):
    results = google.search(query, start = 1,  stop = NUM_GOOGLE_RESULTS, pause = 0.1)
    
    urls = [url for url in results]
    return urls

# Analyze results
def parsePages(urls, wordsInQuery):
    # For example, {"Zeus":500, "Jupiter": 366}
    namesByFrequency = {}

    # Loop through urls, remembering the index for weighting
    for index, url in enumerate(urls):
        try:
            html = google.get_page(url)
        except:
            continue

        if wordsInQuery[0] == "WHEN":
            namesInThisPage = searchHelper.extractDates(html)
        elif wordsInQuery[0] == "WHO":
            namesInThisPage = searchHelper.extractNames(html)

        namesInThisPage = searchHelper.weightNames(namesInThisPage, index, NUM_GOOGLE_RESULTS)
        namesByFrequency = searchHelper.addDicts(namesByFrequency, namesInThisPage)

    namesByPercent = searchHelper.compareNames(namesByFrequency)

    return namesByPercent

if __name__ == "__main__":
    print searchHelper.mostCommon(query("Who played Spiderman?"))
