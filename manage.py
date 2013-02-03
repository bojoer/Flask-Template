from flask import Flask
from application.routes import register_blueprints

app = Flask(__name__)
app.debug = True

register_blueprints(app)

if __name__ == '__main__':
    app.run(port=8080)