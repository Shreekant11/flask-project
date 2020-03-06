from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
@app.route('/Shree')
def Shree():
    return  "Hello Shree"
app.run()