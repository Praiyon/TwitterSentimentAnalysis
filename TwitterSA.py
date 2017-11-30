from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from SentimentAnalysis.twitter_search import TwitterSearch
app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API',
              'test': 'another test'}
    ,
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

data = dict()
outer_data = dict()
def abort_if_todo_doesnt_exist(sentiment_id):
    if sentiment_id not in data:
        abort(404, message="Todo {} doesn't exist".format(sentiment_id))

parser = reqparse.RequestParser()
parser.add_argument('sentiment')



class Todo(Resource):
    def get(self, sentiment_id):
        abort_if_todo_doesnt_exist(sentiment_id)
        return data[sentiment_id]

    def delete(self, sentiment_id):

        del data[sentiment_id]
        return '', 204

    def put(self, sentiment_id):
        args = parser.parse_args()
        sentiment = {'sentiment': args['sentiment']}

        data[sentiment_id] = sentiment
        return sentiment, 201







class TodoList(Resource):
    def get(self):
        return data

    def post(self):
        args = parser.parse_args()
        todo_id = len(data)
        todo_id = 'todo%i' % todo_id
        # data[todo_id] = {'task': args['task']}
        responses = compute(args.sentiment)
        sub_data = dict()
        for i in range (len(responses)):

            sub_data[i] = {'tweet' : responses[i].getTweet(), 'polarity' : responses[i].getPolarity(),
                               'subjectivity' : responses[i].getSubjectivity()}
        data[args.sentiment] = sub_data
        outer_data['data'] = data
        return outer_data, 201

def compute(todo_id):
    search_results = TwitterSearch().search(todo_id)
    return search_results





##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/sentiment')
api.add_resource(Todo, '/sentiment/<sentiment_id>')


if __name__ == '__main__':
    app.run(debug=True)