from flask import Flask
from flask_restful import Api, Resource
from flask import request

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):  # This class inherits from Resource
    def get(self):
        return {"data": "hello"}

    def post(self):
        data = request.data
        data = data.decode('utf-16')
        print(data)
        # return {"data": data}


api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)  # TODO Remove debug=True this for prod
    # app.run(debug=True, ssl_context='adhoc')  # TODO Remove debug=True this for prod
    # app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))

