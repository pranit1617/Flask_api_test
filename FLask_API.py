from flask import Flask
from flask_restful import Resource, Api
from random import randrange

app = Flask(__name__)
api = Api(app)


def get_random_str(low=80, high=100):
    return str(randrange(low, high, 2))


class HelloWorld(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "Hello": "World"
        }


class QOS(Resource):
    def __init__(self):
        pass

    def get(self):
        return{
            "QOS Score": get_random_str()
        }


class QOShistory(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "QOS History":
            {
                "Vaseline":
                [{
                    "Jan": get_random_str(low=60),
                    "Feb": get_random_str(low=60),
                    "March": get_random_str(low=60),
                    "April": get_random_str(low=60),
                    "May": get_random_str(low=60),
                    "June": get_random_str(low=60),
                    "July": get_random_str(low=60),
                    "August": get_random_str(low=60),
                    "September": get_random_str(low=60),
                    "November": get_random_str(low=60),
                    "December": get_random_str(low=60)
                }],

                "Head & Shoulders":
                {
                    "Jan": get_random_str(low=60),
                    "Feb": get_random_str(low=60),
                    "March": get_random_str(low=60),
                    "April": get_random_str(low=60),
                    "May": get_random_str(low=60),
                    "June": get_random_str(low=60),
                    "July": get_random_str(low=60),
                    "August": get_random_str(low=60),
                    "September": get_random_str(low=60),
                    "November": get_random_str(low=60),
                    "December": get_random_str(low=60)
                }
            }
        }


class DQ_issues_to_resolve(Resource):
    def __init__(self):
        pass

    def get(self):
        return {
            "Columns count PRG":
            [{
                "ES": get_random_str(low=60) + "%",
                "IT": get_random_str(low=60) + "%",
                "UK": get_random_str(low=60) + "%",
                "TOtal": get_random_str(low=60) + "%"
            }],

            "Columns count SPO":
            [{
                "ES": get_random_str(low=60) + "%",
                "IT": get_random_str(low=60) + "%",
                "UK": get_random_str(low=60) + "%",
                "TOtal": get_random_str(low=60) + "%"
            }],

            "Null numbers(Age)":
            [{
                "ES": get_random_str(low=60) + "%",
                "IT": get_random_str(low=60) + "%",
                "UK": get_random_str(low=60) + "%",
                "TOtal": get_random_str(low=60) + "%"
            }]
        }


api.add_resource(HelloWorld, '/')
api.add_resource(QOS, '/QOS')
api.add_resource(QOShistory, '/QOShistory')
api.add_resource(DQ_issues_to_resolve, '/DQ_issue_reolve')

if __name__ == "__main__":
    app.run(debug=True)
