from unittest.mock import patch

from nose.tools import assert_is_not_none, assert_dict_equal

from get_bit_bucket_profile_data import GetBitBucketProfileData

DEAFULT_RETURN_STRUCTURE = {
    'public_repos_count': {
        'original': 0,
        'forked': 0,
    },
    'followers_count': 0,
    'open_issues_count': 0,
    'original_repo_commits_count': -1,
    'size_of_account': 0,
    'languages_used': {
        'count': 0,
        'languages': []
    }
}

@patch('get_bit_bucket_profile_data.requests.get')
def test_getting_bit_bucket_data(mock_get):
    """Smoke test to ensure structure of return object in case of success.
    """
    mock_get.return_value.ok = True

    response = GetBitBucketProfileData().call('bit_bucket_username')

    assert_is_not_none(response)
    assert_dict_equal(response, DEAFULT_RETURN_STRUCTURE)

