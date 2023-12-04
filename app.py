from flask import Flask, json, jsonify, request

app = Flask(__name__)

with open('animations.json') as test_file:
    data = json.load(test_file)

@app.route("/directors/<expression>", methods = ['GET'])
def get_director(expression):
    storage = []
    for animation in data['animations']:
        if expression.lower() in animation['Directors'].lower():
            storage.append(animation['Directors'])
    return jsonify(storage)

@app.route("/titles", methods = ['GET'])
def find_animations():
    if request.args:
        storage = []
        for animation in data['animations']:    
            if int(request.args['from'])<=animation['Year of production']<=int(request.args['to']):
                storage.append(animation['Original title'])
        return jsonify(storage)
    else:
        titles = [animation['Original title'] for animation in data['animations']]
        return jsonify(titles)
