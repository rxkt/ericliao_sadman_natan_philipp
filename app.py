from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search/",methods=['GET','POST'])
def showResults():
    print "urmom"
    return render_template("search.html")
if __name__ == "__main__":
    app.debug=True
    app.run()
