from email.mime import application
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    x = 5
    y = 2
    z = x*y
    return render_template('index.html', x=x, y=y, z=z)

@application.route('/javascript')
def javascript():
    return render_template('blog.html')

if __name__=='__main__':
    application.run(debug=True)
