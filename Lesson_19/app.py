from flask import Flask, jsonify ,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
     count= 10
     return render_template(
        "index.html",
        name="Mohammed",
        count=count
    )

@app.route("/search")
def search():
    word = request.args.get("word")
    date = request.args.get("date")
    data = {word:word,date:date}
    return jsonify({'message':'operation succedd','data':data,'code':200})

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/api/greet/<name>",methods=["PUT","PATCH"])
def greetPost(name):
    return jsonify({"message": f"Hello from put and patch method, {name}!"})




# @app.route("/students")
# def students():
#     student = {
#         "name": "Sara",
#         "age": 25,
#         "skills": ["Python", "HTML", "CSS"]
#     }
#     return jsonify(student)


if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8000, debug=True)
    app.run(debug=True)

# flask run --port 8000