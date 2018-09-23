import requests

GIT_HUB_API_USER_URL = 'https://api.github.com/users/{0}'
GIT_HUB_API_REPOS_URL = 'https://api.github.com/users/{0}/repos'
GIT_HUB_API_STARRED_URL = 'https://api.github.com/users/{0}/starred'

class GetGitHubProfileData:

    """Return GitHub profile data in format that can be used by the merge class.

    Aggregate data for the GitHub profile via a few API calls.
    """

    def call(self, username):
        """Call GitHub API for specific user to gather data about them.

        Use data to return a JSON object in format needed for the merged profile.
        """
        profile_response = requests.get(GIT_HUB_API_USER_URL.format(username)).json()
        repos_response = requests.get(GIT_HUB_API_REPOS_URL.format(username)).json()
        starred_response = requests.get(GIT_HUB_API_STARRED_URL.format(username)).json()
        languages, topics = [], []
        stars_received_count, open_issues_count, total_size, = 0, 0, 0
        original_repo_count, forked_repo_count = 0, 0
        for repo in repos_response:
            stars_received_count += repo['stargazers_count']
            open_issues_count += repo['open_issues_count']
            total_size += repo['size']
            if repo['language']:
                languages.append(repo['language'])
            # TODO:
            # topics.append(repo['topics'])
            if repo['fork']:
                forked_repo_count += 1
            else:
                original_repo_count += 1
        languages = list(set(languages))
        # TODO:
        # topics = list(set(topics))
        git_hub_profile = {
            'public_repos_count': {
                'original': original_repo_count,
                'forked': forked_repo_count,
            },
            'followers_count': profile_response['followers'],
            'stars_received_count': stars_received_count,
            'stars_given_count': len(starred_response),
            'open_issues_count': open_issues_count,
            'original_repo_commits_count': -1, # TODO
            'size_of_account': total_size,
            'languages_used': {
                'count': len(languages),
                'languages': languages
            },
            'repo_topics': {
                'count': -1,
                'topics': []
            },
        }
        return git_hub_profile
