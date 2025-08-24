from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/notifications")
def get_notifications():
return jsonify([
{"id":1, "message":"Order 1 shipped"},
{"id":2, "message":"Payment pending for Order 2"}
])


if __name__ == "__main__":
app.run(host="0.0.0.0", port=5005)
