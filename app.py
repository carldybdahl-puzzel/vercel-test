from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<html><body><a href="/null_test">Null Character Test</a></body></html>

@app.route("/null_test")
def null_test():
  return "<html><body>NULL(\u0000)</body></html>"

app.run(debug=True, port=80)
