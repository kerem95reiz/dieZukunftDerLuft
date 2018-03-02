from flask import Flask, request, render_template
# from requests import request

app = Flask(__name__)


@app.route('/<name>')
@app.route('/', methods=['GET', 'POST'])
def home_page(name=None):
    if request.method == 'GET':
        return render_template('findpark.html', name=name)
    else:
        return "Welcome to the best park place finder on the web!"


@app.route('/about')
def about():
    return "We offer the service to find a parkplace"


if __name__ == "__main__":
    app.run("0.0.0.0", 6565)
