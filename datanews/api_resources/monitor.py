from datanews.requestor import Requestor

BASE_URL = 'http://api.datanews.io/v1/monitors/%s'


def _validate_id(id, message):
    if not id:
        raise ValueError(message)


def create(query='', webhook=''):
    if not query:
        raise ValueError('Query must not be empty.')
    url = BASE_URL % 'create'
    return Requestor().request('post', url=url, data={'query': query, 'webhook': webhook})


def list():
    url = BASE_URL % 'list'
    return Requestor().request('get', url=url)


def get(id):
    _validate_id(id, 'Monitor id should not be None.')
    url = BASE_URL % ('/list/%s' % id)
    return Requestor().request('get', url=url)


def delete(id):
    _validate_id(id, 'Monitor id should not be None.')
    url = BASE_URL % ('/delete/%s' % id)
    return Requestor().request('delete', url=url)


def latest(run_id):
    _validate_id(run_id, 'Run id should not be None.')
    url = BASE_URL % ('/latest/%s' % run_id)
    return Requestor().request('get', url=url)
