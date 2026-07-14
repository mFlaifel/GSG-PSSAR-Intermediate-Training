
from flask import Flask,request

app = Flask(__name__)

print("hello")

@app.route("/")
def home():
    return """
    <h1>Welcome</h1>
    <p>This is Flask.</p>
    """

@app.route("/search")
def search():
    print(request)
    q = request.args.get("q")
    return f"You searched for {q}"

app.run()