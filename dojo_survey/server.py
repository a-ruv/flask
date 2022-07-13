from flask import Flask, render_template, request,session,redirect
app = Flask(__name__)
app.secret_key = "shhhhhhh"

@app.route('/')
def load():
    return render_template('index.html')


@app.route("/process", methods = ["POST"])
def process():
    session['name'] = request.form["name"] 
    session['cities'] = request.form['cities'] 
    session['language'] = request.form["languages"] 
    session['comment'] = request.form["comment"] 
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('return.html')

if __name__ =="__main__":
    app.run(debug=True)