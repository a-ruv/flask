import random
from flask import Flask, redirect, render_template,request,session
app = Flask(__name__)
app.secret_key = "shake_and_bake "

@app.route("/")
def game():
    if "answer" not in session:
        session["answer"] = int(random.random()*101)
    return render_template('index.html')

@app.route("/guess", methods=["POST"])
def guess():
    # session['guess'] = int(
    #     request.form['guess'])
    # print(session['answer'])
    if int(request.form["guess"]) > session['answer']:
        session["msg"] = "Too High"
        session["msg_style"] = "incorrect"
    elif int(request.form["guess"]) < session['answer']:
        session["msg"] = "Too Low"
        session["msg_style"] = "incorrect"
    else:
        session["msg"] = "Answer"
        session["msg_style"] = "correct"
        
    
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)