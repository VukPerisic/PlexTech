from pandas import value_counts
from flask import Flask, abort, request
app = Flask(__name__)

@app.route('/hello')
def index():
    if request.args:
        name = request.args.get('name')
        if name:
            return "Hello " + name
    return 'Web App with Python Flask!'

@app.route('/hello-json')
def index1():
    return {"text":"Hello World from Dictionary"}

@app.route('/hello-html')
def index2():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def index3():
    return ('<h1>Hellow World</h1?<p>Subtext</p>', abort(404))

@app.route('/hello/<name>')
def whatevername(name):
    return 'Hello ' + str(name)

@app.route('/hello/<name>/change/<amount>')
def change(name, amount):
    return 'Hello {a}, your change is {b}'.format(a = name, b = 10 - int(amount))

@app.route('/login', methods = ['POST', 'GET'])

@app.route('/reflect', methods = ['POST', 'GET'])
def response():
    payload = request.get_data(as_text = True)        
    return "Hello " + payload

@app.route('/reflect/plex', methods = ['POST', 'GET'])
def response1():
    payload = request.json
    result = {}
    for key in payload:
        new_key, new_value = key, payload[key]
        if isinstance(new_key, str):
            new_key = 'plex_' + new_key
        if isinstance(new_value, str):
            new_value = 'plex_' + new_value
        result[new_key] = new_value
    return result
        
@app.route('/reflect/plex/form', methods = ['POST', 'GET'])
def response2():
    payload = request.json
    result = {}
    for key in payload:
        new_key, new_value = 'plex_' + key, 'plex_' + payload[key]
        result[new_key] = new_value
    return result
    

app.run(host = '0.0.0.0', port=81)