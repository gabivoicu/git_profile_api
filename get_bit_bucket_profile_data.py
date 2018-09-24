import requests

BIT_BUCKET_API_REPOS_URL = 'https://api.bitbucket.org/2.0/repositories/{0}'
BIT_BUCKET_API_FOLLOWERS_URL = 'https://api.bitbucket.org/2.0/users/{0}/followers'

class GetBitBucketProfileData:

    """Return BitBucket profile data in format that can be used by the merge class.

    Aggregate data for the BitBucket profile via a few API calls.
    """

    def call(self, username):
        """Call BitBucket API for specific user to gather data about them.

        Use data to return a JSON object in format needed for the merged profile.
        """
        repos_response = requests.get(BIT_BUCKET_API_REPOS_URL.format(username)).json()
        folowers_response = requests.get(BIT_BUCKET_API_FOLLOWERS_URL.format(username)).json()
        languages = []
        open_issues_count, total_size = 0, 0
        for repo in repos_response['values']:
            if repo['has_issues']:
                issues_response = requests.get(repo['links']['issues']['href']).json()
                open_issues_count += len(issues_response['values'])
            total_size += repo['size']
            if repo['language']:
                languages.append(repo['language'].lower())
        languages = list(set(languages))
        # TODO:
        # Figure out original vs forked repos for the 2.0 version of the API. So far, I have not found a way to figure out
        # if a give repo is a fork or original based on the info returned on BIT_BUCKET_API_REPOS_URL.
        bit_bucket_profile = {
            'public_repos_count': {
                'original': len(repos_response['values']),
                'forked': -1,
            },
            'followers_count': len(folowers_response['values']),
            'open_issues_count': open_issues_count,
            'original_repo_commits_count': -1, # TODO
            'size_of_account': total_size,
            'languages_used': {
                'count': len(languages),
                'languages': languages
            }
        }
        return bit_bucket_profile
