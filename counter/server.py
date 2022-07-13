from flask import Flask,render_template,redirect,session
app = Flask(__name__)
app.secret_key = "shake_and_bake "

@app.route('/')
def showcounter():
    if "counter" in session:
        session['counter'] +=1
    else:
        session['counter'] = 1
    return render_template("index.html")

@app.route("/destroy_session")
def reset():
    session["counter"] = 0
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['counter'] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
