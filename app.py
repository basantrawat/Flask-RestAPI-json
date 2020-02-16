from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Configuring JSON
with open('details.json', 'r') as c:
    userDetails = json.load(c)["users"]


@app.route('/userdetails/api/users', methods=['GET'])
def get():
    if(request.method == 'GET'):
        return jsonify(userDetails)
    else:
        return "Page Not Found", 404


@app.route('/userdetails/api/users/<string:name>', methods=['GET'])
def getbyname(name):
    if(request.method == 'GET'):
        for user in userDetails:
            if(user['name'] == name):
                data = user
                return jsonify({'data': data})
            else:
                return "User with name {} not found in DB".format(name), 404


@app.route('/userdetails/api/users', methods=['POST'])
def postfunc():
    if not request.json or not 'name' in request.json:
        return "Error with Bad Request"
    user = {
        'name': request.json["name"],
        'age': request.json["age"],
        'gender': request.json["gender"]
    }

    userDetails.append(user)
    return jsonify({'user': user}), 201


@app.route('/userdetails/api/users/<string:name>', methods=['PUT'])
def put(name):
    user = [user for user in userDetails if user['name'] == name]
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['age'] = request.json.get('age', user[0]['age'])
    user[0]['gender'] = request.json.get('gender', user[0]['gender'])
    return jsonify({'data': user[0]})


@app.route('/userdetails/api/users/<string:name>', methods=['DELETE'])
def delete(name):
    data = [user for user in userDetails if user["name"] != name]
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug=True)
