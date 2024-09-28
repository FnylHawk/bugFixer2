from flask import Flask
from routes.bugfixer import bugfixer

app = Flask(__name__)
app.register_blueprint(bugfixer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)