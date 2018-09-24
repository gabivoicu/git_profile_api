import requests

class MergeGitProfiles:

    """Return a merged git profile when provided data for GitHub and BitBucket accounts.
    """

    def call(self, git_hub_data, bit_bucket_data):
        """Return a merged git profile when provided data for GitHub and BitBucket accounts.
        """
        languages_used = list(set(git_hub_data['languages_used']['languages'] + bit_bucket_data['languages_used']['languages']))
        return {
            'public_repos_count': {
                'original': git_hub_data['public_repos_count']['original'] + bit_bucket_data['public_repos_count']['original'],
                'forked': git_hub_data['public_repos_count']['forked'] + bit_bucket_data['public_repos_count']['forked'],
            },
            'followers_count': git_hub_data['followers_count'] + bit_bucket_data['followers_count'],
            'stars_received_count': git_hub_data['stars_received_count'],
            'stars_given_count': git_hub_data['stars_given_count'],
            'open_issues_count': git_hub_data['open_issues_count'] + bit_bucket_data['open_issues_count'],
            'original_repo_commits_count': git_hub_data['original_repo_commits_count'] + bit_bucket_data['original_repo_commits_count'],
            'size_of_account': git_hub_data['size_of_account'] + bit_bucket_data['size_of_account'],
            'languages_used': {
                'count': len(languages_used),
                'languages': languages_used
            },
            'repo_topics': {
                'count': git_hub_data['repo_topics']['count'],
                'topics': git_hub_data['repo_topics']['topics']
            },
        }
