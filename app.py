from flask import Flask
App = Flask(__name__)
@App.route('/')
def home():
    return "Hello World"
if __name__ == '__main__':
    App.run(host='0.0.0.0', port=5000)