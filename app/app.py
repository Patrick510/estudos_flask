import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html', name="Upload de Imagem")

@app.route("/submit", methods=["POST"])
def submit():
    imagem = request.files['image'] 

    if imagem:
        caminho = f"./uploads/{imagem.filename.split('.')[0]}_{datetime.now().strftime('%Y-%m-%d')}.{imagem.filename.split('.')[-1]}"  
        os.makedirs('./uploads', exist_ok=True) 
        imagem.save(caminho)
        return render_template('form.html', name="Upload de Imagem", message=f"Imagem salva em {caminho}")
    return "Nenhuma imagem recebida"

if __name__ == "__main__":
    app.run(debug=True)
