from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)
id_aula = 0
lista_aulas = []

@app.route("/")
def home():
  return render_template("index.html", name="Home page", lista_aulas=lista_aulas)

@app.route("/form")
def form():
  return render_template("form.html", name="Form", lista_aulas=lista_aulas)

@app.route("/submit", methods=["POST"])
def submit():
  global id_aula
  materia = request.form.get("materia")
  professor = request.form.get("professor")
  data = request.form.get("data")
  id_aula += 1
  
  lista_aulas.append({"id": id_aula, "materia": materia, "professor": professor, "data": data})
  
  return redirect(url_for('form'))

@app.route("/delete/<int:aula_id>", methods=["DELETE"])
def delete(aula_id):
  global lista_aulas
  lista_aulas = [aula for aula in lista_aulas if aula["id"] != aula_id]

  return jsonify({"message": "Materia deletada com sucesso"}), 200

if __name__ == "__main__":
  app.run(debug=True)