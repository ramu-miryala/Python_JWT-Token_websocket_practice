from flask import Flask,  request , jsonify

app = Flask(__name__)

@app.route('/hello' ,methods =['GET'])
def hello():
    return jsonify({"message":"Hello Ramu "})

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name','Guest')
    qualification = data.get('qualification','Not-specified')
    location = data.get('location','Not-specified')
    return jsonify({"message" : f"Hello ,{name}!",
                    "qualification":qualification,
                    "location":location})



if __name__ == '__main__':
    app.run(debug = True)

    