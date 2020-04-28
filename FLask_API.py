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
        return{
            "QOS Score":"96.6"
        }

class QOShistory(Resource):
    def __init__(self):
        pass
    def get(self):
        return{
            "QOS History":
            {
                "Vaseline":
               [{
                    "Jan":0.85,
                    "Feb":0.86,
                    "March":0.87,
                    "April":0.875,
                    "May":0.9,
                    "June":0.89,
                    "July":0.88,
                    "August":0.89,
                    "September":0.9,
                    "November":0.93,
                    "December":0.94
                }],
                
                "Head & Shoulders":
                {
                    "Jan":"0.75",
                    "Feb":"0.77",
                    "March":"0.77",
                    "April":"0.775",
                    "May":"0.8",
                    "June":"0.89",
                    "July":"0.88",
                    "August":"0.9",
                    "September":"0.91",
                    "November":"0.92",
                    "December":"0.94"
                }
            }
        }

class DQ_issues_to_resolve(Resource):
    def __init__(self):
        pass
    def get(self):
        return{
            "Sensor":"Columns count PRG"
            [{
                "ES":"100%",
                "IT":"9%",
                "UK":"4%",
                "TOtal":"38%"
            }],

            "Sensor":"Columns count SPO"
            [{
                "ES":"100%",
                "IT":"9%",
                "UK":"4%",
                "TOtal":"38%"
            }],

            "Sensor":"Null numbers(Age)"
            [{
                "ES":"100%",
                "IT":"55%",
                "UK":"100%",
                "TOtal":"85%"
            }]
        }




api.add_resource(HelloWorld,'/')
api.add_resource(QOS,'/QOS')
api.add_resource(QOShistory,'/QOShistory')
api.add_resource(DQ_issues_to_resolve,'/DQ_issue_reolve')

if __name__ == "__main__":
    app.run(debug=True)
