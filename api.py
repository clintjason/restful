from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__) # instantiate a flask application
api = Api(app)	# instantiate the Api class

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


'''
	To access the these resources use curl or the get and PUT methods in the request obj
'''