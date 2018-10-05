## Run the server

Clone the repo
`git clone https://github.com/gabivoicu/git_profile_api.git`

From inside the repo
`cd git_profile_api/`

Run
`python3 -m venv venv`

`. venv/bin/activate`

`pip install requirements.txt`

And then start the server:
`FLASK_ENV=development flask run`

To test, you can use this URI via a `GET` request:

`/git_profile/?github_username=gabivoicu&bitbucket_username=mcfletch`



## Things learned and TODOS:

- BitBucket does not have a concept of stars

- BitBucket does not have a concept of topics

- GitHub Topics: they appear to only be visible to the logged in owner of the repo, based on https://developer.github.com/v3/repos/#list-all-topics-for-a-repository. Further investigation is required. Alternatively,
the GitHub GraphQL might have this information but that would potentially require rewriting `GetGitHubProfileData`.

- Pagination: Due to time constraints, I have so far coded the absolute happy path. Pagination has been ignored entirely. To add pagination,
look up which of the endpoints support pagination and update calls to those endpoints to be made untill all the data has been read.

- Forked repos in BitBucket: on the repositories call it is unclear wether a repo is original or a fork. I have searched the BitBucket documentation far and wide and could not figure out a spot where that information is available. One potential hypothesis is that the 2.0 version of the API does not show that information _yet_ (this based on a support ticket I came across). This is a little strange because 2.0 is the current version and 1.0 is deprecated/in the process of being retired entirely.

- Languages used in GitHub: Due to time constraints the languages aggregated for the GitHub profile are just the top languages returned on the repositories call. To get all languages, a new call will need to be made for each repo.

- TESTS: Due to time constraints no tests have been added. Tests are needed for these scenarios:
  - happy path: valid usernames are provided, calls to the GitHub and BitBucket APIs are stubbed and the merged profile is returned in the expected format
  - one or both of the usernames is not provided; server should return code `400` and appropriate message
  - one or both of the APIs is down; server should return code `503` and appropriate message; code should be added to implement this behavior
  - at least one of the API call fails due permissions; server should return code `401/403` and appropriate message; code should be added to implement this behavior; in case any of the data calls fail, we should return an error message because the integrity of the data has been compromised.
