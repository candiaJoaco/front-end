from flask import Flask, request, jsonify
from main import SimpleLangGraphApp  # Asegúrate de importar correctamente

app = Flask(__name__)

PROJECT_ID = "ai-products-by-conauti-436905"
LOCATION = "us-central1"

agent = SimpleLangGraphApp(project=PROJECT_ID, location=LOCATION)
agent.set_up()

@app.route('/query', methods=['POST'])
def query():
    message = request.json.get("message")
    if not message:
        return jsonify({"error": "Message is required"}), 400
    response = agent.query(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)