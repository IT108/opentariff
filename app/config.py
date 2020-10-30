import os

params = {
    'branch': 'test',
    'commit': 'test',
}


def config_from_env():
    global params
    params['branch'] = os.environ.get('BRANCH', params['branch'])
    params['commit'] = os.environ.get('COMMIT', params['commit'])[:7]
