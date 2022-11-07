from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route("/add_receipt")
def add_receipt():
    return render_template("add_receipt.html")


@app.route("/half_annually_payment")
def half_annually_payment():
    return render_template("half_annually_payment.html")

if __name__ == '__main__':
    app.run(debug=True)
