from datanews.requestor import Requestor

BASE_URL = 'http://api.datanews.io/v1/%s'


def _build_params(params, q=None, from_date=None, to_date=None, source=None, country=None, language=None, topic=None, page=None, size=None, sortBy=None):
    if q is not None:
        if type(q) is not str:
            raise ValueError('Query must be a string object.')
        params['q'] = q

    if from_date is not None:
        if type(from_date) is not str:
            raise ValueError('From date must be a string object.')
        params['from'] = from_date

    if to_date is not None:
        if type(to_date) is not str:
            raise ValueError('To date must be a string object.')
        params['to'] = to_date

    if source is not None:
        if type(source) is str:
            source = [source]
        elif type(source) is not list:
            raise ValueError('Source must be a string or a list of strings object.')
        params['source'] = source

    if country is not None:
        if type(country) is str:
            country = [country]
        elif type(country) is not list:
            raise ValueError('Source must be a string or a list of strings object.')
        params['country'] = country

    if language is not None:
        if type(language) is str:
            language = [language]
        elif type(language) is not list:
            raise ValueError('Source must be a string or a list of strings object.')
        params['language'] = language

    if topic is not None:
        if type(topic) is str:
            topic = [topic]
        elif type(topic) is not list:
            raise ValueError('Source must be a string or a list of strings object.')
        params['topic'] = topic

    if page is not None:
        if type(page) is not int or page < 0:
            raise ValueError('Page must be a positive integer.')
        params['page'] = page

    if size is not None:
        if type(size) is not int or (size < 0 or size > 100):
            raise ValueError('Size must be a positive integer from 1 to 100.')
        params['size'] = size

    if sortBy is not None:
        if sortBy != 'relevance' and sortBy != 'date':
            raise ValueError('SortBy must equal \'relevance\' or \'date\'')
        params['sortBy'] = sortBy

    return params


def headlines(q=None, source=None, country=None, language=None, topic=None, page=None, size=None, sortBy=None):
    url = BASE_URL % 'headlines'
    params = {}
    _build_params(params, q=q, source=source, country=country, language=language, topic=topic,
                  page=page, size=size, sortBy=sortBy)
    return Requestor().request('get', url=url, params=params)


def news(q=None, from_date=None, to_date=None, source=None, country=None, language=None, topic=None,
         page=None, size=None, sortBy=None):
    url = BASE_URL % 'news'
    params = {}
    _build_params(params, q=q, from_date=from_date, to_date=to_date, source=source, country=country, language=language,
                  topic=topic, page=page, size=size, sortBy=sortBy)
    return Requestor().request('get', url=url, params=params)


def sources(country=None, language=None, topic=None, page=None, size=None):
    url = BASE_URL % 'sources'
    params = {}
    _build_params(params, country=country, language=language, topic=topic, page=page, size=size)
    return Requestor().request('get', url=url, params=params)
