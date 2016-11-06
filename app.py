from flask import Flask, render_template, send_from_directory
from scripts import annotations


app = Flask(__name__, static_url_path='/static')


# Home page
@app.route('/')
def home():
    message = 'Welcome to Jar-Gone'
    print ("home page")
    return render_template('index.html', message=message)

@app.route('/getTxt')
def getTxt():
	print ("GOT HERE")
	return send_from_directory('static', 'data/medical_consult.txt')

@app.route('/getAnnotations')
def getAnnotations():
	print("IN ANNOTATIONS")
	result  = annotations.get_definitions(annotations.open_file())
	print("RESULT:\n",  result)

	print("FINISHED", type(result))
	thefile = open('test.json', 'w')
	for item in result:
 		thefile.write("%s\n" % item)
	return str(result);


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)