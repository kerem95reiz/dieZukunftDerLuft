from flask import Flask, request, render_template
from parkPlaceFinding.riskCalc import getRisk

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('findpark.html')


@app.route('/findparkplace', methods=['GET', 'POST'])
def findparkplace():
    address = request.form['address']
    prox = request.form['proximity']
    # result = getRisk(address)
    result = "Address Not found"
    return result


if __name__ == "__main__":
    app.run("0.0.0.0", 6565)
