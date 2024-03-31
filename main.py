from flask import Flask, render_template, request
app = Flask(__name__)
@app.get('/')
def showlogin():
    return render_template('index.html')

@app.post('/main')
def main_page():
    usname = request.form['username']
    return render_template('page2.html',output = usname)

app.run(debug=True)