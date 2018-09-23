import requests

GIT_HUB_API_BASE_URL = 'https://api.github.com/users/'

class GetGitHubProfileData:

    """
    """

    def call(self, username):
        """
        """
        url = GIT_HUB_API_BASE_URL + username
        profile_response = requests.get(url).json()
        repos_url = profile_response['repos_url']
        starred_url = url + '/starred'
        repos_response = requests.get(repos_url).json()
        starred_response = requests.get(starred_url).json()
        languages, topics = [], []
        stars_received_count, languages_count, topics_count, total_size = 0, 0, 0, 0
        original_repo_count, forked_repo_count = 0, 0
        for repo in repos_response:
            stars_received_count += repo['stargazers_count']
            # languages_count += repo['stargazers_count']
            # topics_count += repo['stargazers_count']
            total_size += repo['size']
            if repo['language']:
                languages.append(repo['language'])
            # topics.append(repo['language'])
            if repo['fork']:
                forked_repo_count += 1
            else:
                original_repo_count += 1
        languages = list(set(languages))
        git_hub_profile = {
            'public_repos_count': {
                'original': original_repo_count,
                'forked': forked_repo_count,
            },
            'followers_count': profile_response['followers'],
            'stars_received_count': stars_received_count,
            'stars_given_count': len(starred_response),
            'open_issues_count': 0,
            'original_repo_commits_count': 0,
            'size_of_account': total_size,
            'languages_used': {
                'count': len(languages),
                'languages': languages
            },
            'repo_topics': {
                'count': 0,
                'topics': []
            },
        }
        print(git_hub_profile)
        return git_hub_profile
