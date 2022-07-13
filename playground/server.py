from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    return render_template('index.html',num = 15, color = "blue")

@app.route("/play/<int:num>")
def play1(num):
    return render_template('index.html',num = num, color = "blue")

@app.route("/play/<int:num>/<string:color>")
def play2(num,color):
    return render_template('index.html',num = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)