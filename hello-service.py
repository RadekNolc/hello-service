from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name):
    message = f'Hello {name}! How are you?'
    response = f'{{ "message": "{message}"}}\r\n'
    code = 200
    return response, code, {'Content-Type': 'application/json'}

if (__name__ == '__main__'):
    app.run(host="0.0.0.0")