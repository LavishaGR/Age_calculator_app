from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def app_route():
    return render_template('age_calculator.html')
@app.route("/about)
def aboutme():
    return render_template("aboutme.html")

    if __name__ == '__main__':
        app.run(debug=True)