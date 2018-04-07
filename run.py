from flask import Flask
from flask_restful import Resource, Api

from routes.ping_route import PingRoute

app = Flask(__name__)
api = Api(app)

api.add_resource(PingRoute, '/ping')

if __name__ == '__main__':
    app.run()