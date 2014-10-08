from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search",methods=['GET','POST'])
def showResults():
    results = request.args.get("input");
    ##utilize dictionary to create a string
    ##based on the type of search
    for element in request.args.keys():
        if element=="submit":
            ##submit mode-- display all results
            print "submit flag"
        elif element=="lucky":
            ##i'm feeling lucky mode-- display the one most
            ##important/occuring answer
            print "lucky flag"
    return render_template("search.html",string=results)


if __name__ == "__main__":
    app.debug=True
    app.run()
