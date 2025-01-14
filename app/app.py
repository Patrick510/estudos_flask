from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
id_text = 0
texts = []

@app.route("/")
def form():
  return render_template('form.html', name="Form")

@app.route("/home")
def home():
  return render_template("index.html", name="Home", texts=texts)

@app.route("/submit", methods=["POST"])
def submit():
  global id_text
  text = request.form.get("text")
  if text:
    id_text+=1
    date = datetime.now().strftime("%Y-%m-%d")
    texts.append({"id": id_text, "text":text, "date":date})
    message = "Texto salvo com sucesso"
  else:
    message = "Texto nao salvo"
  return render_template("form.html", name="Form", message=message, texts=texts)

if __name__ == "__main__":
  app.run(debug=True)
