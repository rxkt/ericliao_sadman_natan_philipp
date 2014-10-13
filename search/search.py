import google
import searchHelper

# Odd number to make weighting easier
NUM_GOOGLE_RESULTS = 3

# Main function
def query(searchStr):
    pages = getPages(searchStr)
    names = parsePages(pages)
    return names

# Searches Google for query
def getPages(query):
    results = google.search(query, start = 1,  stop = NUM_GOOGLE_RESULTS, pause = 0.1)
    
    urls = [url for url in results]
    return urls

# Analyze results
def parsePages(urls):
    # For example, {"Zeus":500, "Jupiter": 366}
    namesByFrequency = {}

    # Loop through urls, remembering the index for weighting
    for index, url in enumerate(urls):
        html = google.get_page(url)
        namesInThisPage = searchHelper.extractNames(html)
        namesInThisPage = searchHelper.weightNames(namesInThisPage, index, NUM_GOOGLE_RESULTS)
        namesByFrequency = searchHelper.addDicts(namesByFrequency, namesInThisPage)

    namesByPercent = searchHelper.compareNames(namesByFrequency)

    return namesByPercent

if __name__ == "__main__":
    print searchHelper.mostCommon(query("Who played Spiderman?"))
