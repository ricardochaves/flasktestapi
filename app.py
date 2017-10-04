from flask import Flask, request, jsonify, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/homeglobomais/", methods=['POST', 'GET'])
def homegmais():
    if request.method == "GET":
        obj = {'nome': 'teste', 'id': 1}
        response = jsonify(obj)
        response.status_code = 200
        return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
