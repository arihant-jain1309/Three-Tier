from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/orders")
def get_orders():
return jsonify([
{"id":1, "product":"Laptop", "user":"John"},
{"id":2, "product":"Mouse", "user":"Jane"}
])


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5003)
