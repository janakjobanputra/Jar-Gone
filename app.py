from flask import Flask, render_template, send_from_directory
from scripts import annotations


app = Flask(__name__, static_url_path='/static')


# Home page
@app.route('/')
def home():
    message = 'Welcome to Jar-Gone'
    return render_template('index.html', message=message)

@app.route('/getTxt')
def getTxt():
	# print ("GOT HERE")
	return send_from_directory("/data", "sampleTextBlock.txt")

@app.route('/getAnnotations')
def getAnnotations():
	print("IN ANNOTATIONS")
	result  = annotations.get_definitions(annotations.open_file())
	print("RESULT",  result)
	return result;


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)