from flask import Flask, request, render_template
# from requests import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    # user_input = request.form['adress']
    return render_template('findpark.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    xxx = request.form
    address = request.form['address']
    prox = request.form['proximity']
    return request.form.__str__()


@app.route('/process_data')
def process_user_input():
    return "sdfsdf"

if __name__ == "__main__":
    app.run("0.0.0.0", 6565)
