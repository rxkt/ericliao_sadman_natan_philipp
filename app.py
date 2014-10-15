from flask import Flask, render_template, request

# note that this only works because I created an empty __init__.py in search/
# source: http://stackoverflow.com/a/1260813/805556
from search import search
from search import searchHelper

app = Flask(__name__)
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search",methods=['GET','POST'])
def showResults():
    if request.method == "GET":
        # extract search string from GET parameter
        searchStr = request.args.get("query");
    elif request.method == "POST":
        searchStr = request.form.get("query");
    print "SEARCHING FOR " + searchStr
    # use search module we built to get the answer in the form of a dict, name:freq
    results = search.query(searchStr);

    # utilize dictionary to create a string
    # based on the type of search
    #for element in request.args.keys():
    #    if element=="submit":
    #        resultsType = "submit"
    #    elif element=="lucky":
    #        # i'm feeling lucky mode-- display the one most
            # important/occuring answer
    #        resultsType = "lucky"

    # template gets two parameters: results (dict name:freq), searchStr (query)
    # this is a regular search through the website.
    print "got answer: " + results
    if request.method == "GET":
        #return render_template("search.html", results = results, searchStr = searchStr)
        return render_template("index.html", results = results, searchStr = searchStr)

    # AJAX makes POST requests, and for AJAX requests we return the answer without any HTML.
    elif request.method == "POST":
        return results


if __name__ == "__main__":
    app.debug=True
    app.run()
