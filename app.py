from flask import Flask, request, jsonify, render_template
from query_data import main as query_model  # Import your backend query logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query_text = data.get('query', '')

    # Call your backend logic to get the response and sources
    response_text, sources = query_model(query_text)

    # Format the output for the response box
    formatted_sources = "\n".join(sources)
    response = f"{response_text}\n\nResources:\n{formatted_sources}"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

