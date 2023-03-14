from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template('andro.html')

@app.route('/andro')
def hal_1(): 
	return render_template('andro.html') 

@app.route('/ios')
def hal_2(): 
	return render_template('ios.html')

@app.route('/banding')
def hal_3():
	return render_template('banding.html')

if __name__== "__main__":
	app.run (debug = True)