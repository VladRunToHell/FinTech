from flask import Flask
from flask import render_template
import jyserver.flask as jsf

app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        self.count = 0

@app.route('/')
def index():
    return  render_template('index.html')

if __name__ == '__main__':
    app.run()