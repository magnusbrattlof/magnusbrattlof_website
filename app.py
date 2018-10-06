from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import request

application = Flask(__name__)

@application.route('/')
def index():

    return render_template('index.html', 
	ip=request.remote_addr, d=str(request.headers))

@application.route('/docs')
def docs():
    return render_template('docs/index.html')

@application.route('/docs/examples')
def docs_examples():
    return render_template('docs/examples/index.html')

if __name__ == '__main__':
    application.run('192.168.2.10')
