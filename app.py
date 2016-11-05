from flask import Flask, render_template


app = Flask(__name__)


# Home page
@app.route('/')
def home():
    message = 'Welcome to Jar-Gone'
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)