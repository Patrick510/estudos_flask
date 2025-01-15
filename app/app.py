from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

texts = [
    {"id": 1, "text": "Texto exemplo 1"},
    {"id": 2, "text": "Texto exemplo 2"},
    {"id": 3, "text": "Texto exemplo 3"}
]

@app.route('/')
def home():
    return render_template('index.html', texts=texts, name="Flask")

@app.route('/delete/<int:text_id>', methods=['DELETE'])
def delete_text(text_id):
    global texts
    texts = [text for text in texts if text["id"] != text_id] 
    return jsonify({"message": "Texto excluído com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
