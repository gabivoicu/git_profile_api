import requests

from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

class GitProfile(Resource):

    """Return a merged git profile for a user.

    Given a valid BitBucket and a valid GitHub usernames, the class will return a merged profile
    of the user in JSON format.
    """

    def get(self):
        """Return a merged git profile provided two valid git usernames for GitHub and BitBucket.

        This method orchestrates all the steps needed to create the merged profile: read the usernames
        from the query string, validate the usernames, call GitHub and BitBucket for the relevant information
        for each username and return a JSON of the merged profile.
        """
        github_username, bitbucket_username = self.get_usernames()
        if (github_username == None) or (bitbucket_username == None):
            return { 'message': 'A merged user profile could not be returned. Please provide a github_username and a bitbucket_username key.'}, 400
        github_response = requests.get('https://api.github.com/users/gabivoicu')
        bitbucket_response = requests.get('https://api.bitbucket.org/1.0/users/muntzen')
        return bitbucket_response.json()

    def get_usernames(self):
        """Get the git usernames.

        Read the git usernames from the query string. If one or more of the usernames if not
        provided, return None for its value.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('github_username')
        parser.add_argument('bitbucket_username')
        args = parser.parse_args()
        github = args.get('github_username', None)
        bitbucket = args.get('bitbucket_username', None)
        return github, bitbucket

api.add_resource(GitProfile, '/git_profile/')

if __name__ == '__main__':
    app.run(debug=True)
