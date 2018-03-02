from flask import Flask, request, render_template
# from requests import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    # user_input = request.form['adress']
    return render_template('findpark.html')
    # return user_input


@app.route('/about', methods=['GET', 'POST'])
def about():
    xxx = request
    address = request.form['adress']
    prox = request.form['proximity']
    return request.form.__str__()

    # return wer
    # return "We offer the service to find a parkplace"


@app.route('/process_data')
def process_user_input():
    return "sdfsdf"

if __name__ == "__main__":
    app.run("0.0.0.0", 6565)
