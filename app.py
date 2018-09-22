from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

class GitProfile(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('github_username', type=str, help='GitHub username needs to be a string value.')
        parser.add_argument('bitbucket_username', type=str, help='BitBucket username needs to be a string value.')
        args = parser.parse_args()
        github_username = args.get('github_username', None)
        bitbucket_username = args.get('bitbucket_username', None)
        if (github_username == None) or (bitbucket_username == None):
            return { 'message': 'A merged user profile could not be returned. Please provide a github_username and a bitbucket_username key.'}, 400
        return args

api.add_resource(GitProfile, '/git_profile/')

if __name__ == '__main__':
    app.run(debug=True)
