from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    name = ""
    return render_template("home.html", name=name)

@app.route("/baibac")
def baibac():
    return render_template("baibac.html")
    
@app.route("/thahoa")
def tahoa():
    return render_template("thahoa.html")

@app.route("/taixiu")
def taixiu():
    return render_template("taixiu.html")    

@app.route("/index")
def index():
    return render_template("index.html")   

if __name__ == "__main__":
    app.run(debug=True)
