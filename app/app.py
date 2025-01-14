from flask import render_template, Flask, request
from datetime import datetime

app = Flask(__name__)
attempts = []
attempt = 0
message = ["Login successfully", "Login failed", "Limit attempts exceeded", "Please fill in both fields"]
validate = ["user", "admin"]

@app.route("/")
def home():
    return render_template("index.html", name="Login")

@app.route("/login", methods=["POST"])
def login():
    global attempt
    user = request.form.get("user")
    password = request.form.get("pass")
    
    if attempt == 3:
        return render_template("index.html", message=message[2], disable=True)
    
    if user and password:
        if user == validate[0] and password == validate[1]:
            attempts.append({"attempt": attempt, "user": user, "date": datetime.now().strftime("%Y-%m-%d")})
            attempt = 0 
            return render_template("index.html", message=message[0], disable=False)
        else:
            attempt += 1
            attempts.append({"attempt": attempt, "user": user, "date": datetime.now().strftime("%Y-%m-%d")})
            return render_template("index.html", message=message[1])

    attempt = 0
    return render_template("index.html", message=message[3], disable=False)

if __name__ == "__main__":
    app.run(debug=True)
