from flask import Flask, render_template, request
from search import search
from search import nameFind

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search",methods=['GET','POST'])
def showResults():
    # the search string
    searchStr = request.args.get("search");

    # use the search module we built to get the answer in the form of a dict, name:freq
    result = search.query(searchStr);

    # utilize dictionary to create a string
    # based on the type of search
    for element in request.args.keys():
        if element=="submit":
            resultsType = "submit"
        elif element=="lucky":
            # i'm feeling lucky mode-- display the one most
            # important/occuring answer
            resultsType = "lucky"
    return render_template("search.html", results = results, resultsType = resultsType)


if __name__ == "__main__":
    app.debug=True
    app.run()
