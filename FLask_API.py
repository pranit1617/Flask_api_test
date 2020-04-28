from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def __init__(self):
        pass
    
    def get(self):
        
            return {
                "Hello":"World"
            }


class QOS(Resource):
    def __init__(self):
        pass
    def get(self):
        return {
            "QOS": "96.9"
        }

    
class QOSHistory(Resource):
    def __init__(self):
        pass
    def get(self):
        return {
            "QOS-History": {
                "Jan": "99.0",
                "Feb": "98.7",
                "Mar": "97.7"
            }
        }

api.add_resource(HelloWorld,'/')
api.add_resource(QOS,'/qos')
api.add_resource(QOSHistory,'/qos-history')

if __name__ == "__main__":
    app.run(debug=True)
