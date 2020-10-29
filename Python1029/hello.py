from flask import Flask, render_template, request #追加

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask!"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_manager", methods=["POST"])
def login_manager():
    return "ようこそ" + request.form["username"] + "さん"
    
if __name__ == "__main__":
    app.run()