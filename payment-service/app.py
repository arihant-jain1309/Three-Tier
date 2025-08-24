from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/payments")
def get_payments():
return jsonify([
{"id":1, "order_id":1, "status":"Paid"},
{"id":2, "order_id":2, "status":"Pending"}
])


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5004)
