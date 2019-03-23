

from flask import Flask, render_template ,request
from topsis import task
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/formCalcula')
def formCalcula():
    return render_template('index.html')

@app.route('/calcula', methods=['GET','POST'])
def calculaTopsis():
    if request.method == 'POST':
        f = request.files['file']
        
    return task.getTopSisDataframe(f)

if __name__ == '__main__':
    app.run()


