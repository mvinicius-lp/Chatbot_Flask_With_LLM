from flask import Flask, render_template, request, jsonify
from model import query_model  # Importa a função que usa o modelo LLM

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    llm_response = query_model(user_message)  # Chama o modelo para gerar a resposta
    return jsonify({'response': llm_response})

if __name__ == '__main__':
    app.run()
