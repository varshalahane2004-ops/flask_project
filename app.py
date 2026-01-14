from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/github-webhook/", methods=["POST"])
def github_webhook():
    data = request.json
    print("GitHub Webhook Received")
    print(data)
    return "OK", 200

if __name__ == "_main_":
    app.run(debug=True, port=8080)

