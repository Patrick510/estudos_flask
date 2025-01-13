from flask import Flask, render_template, request

app = Flask(__name__)
all_text = []

@app.route("/")
def home():
  return render_template('form.html', name="Form")

@app.route("/submit", methods=["POST"])
def submit():
  text = request.form.get("text")
  if text:
    all_text.append(text)
    message = "Texto salvo com sucesso"
  else:
    message = "Texto nao salvo"
  return render_template("form.html", name="Form", message=message)

if __name__ == "__main__":
  app.run(debug=True)
