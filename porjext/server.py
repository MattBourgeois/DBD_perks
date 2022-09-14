from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('dex.html')

@app.route('/flash')
def flas():
	return render_template('flash.html')

@app.route('/flashlight')
def flash():
	return redirect('/flash')


if __name__ == '__main__':
	app.run(debug = True)