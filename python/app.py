from flask import Flask, request, jsonify ,render_template
from llm import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate_response', methods=['POST'])
def generate_response():
    request_data = request.get_json()
    prompts = request_data.get('prompts', [])



    result= get_result(prompts)


    # Return response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,port=7000)
