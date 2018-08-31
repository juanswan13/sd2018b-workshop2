import logging
def get_user_info(username=None):
    return {"user_info": username}

def get_commits_info(username=None, time_range=None):
    return [{'commits_count': 10, 'yyyymmdd_date': '20180101'},
            {'commits_count': 10, 'yyyymmdd_date': '20180102'}]

def get_users_commits_info(org=None, repo=None, user=None):
        logging.debug('organization=%s', org)
        logging.debug('repo=%s', repo)
        logging.debug('user=%s', user)
        return [{'organization': org, 'repository': repo, "user_name": user},
        {'organization': org, 'repository': repo, "user_name": user}]
