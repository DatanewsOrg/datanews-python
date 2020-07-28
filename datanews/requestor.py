import datanews
import requests

from urllib.parse import urlencode


class Requestor(object):
    def __init__(self):
        self.api_key = datanews.api_key

    def request(self, method, url, params=None, data=None):
        self._validate_key(self.api_key)
        if method == 'get':
            return self._get(url, params)
        elif method == 'post':
            return self._post(url, data)
        elif method == 'delete':
            return self._delete(url, data)
        else:
            raise ValueError('Invalid method value \'%s\'' % method)

    def _get(self, url, params):
        if params:
            qstring = urlencode(params, doseq=True)
            url = url + '?' + qstring
        return self._handle_response(
            requests.get(url, headers=self._build_headers()))

    def _post(self, url, data):
        return self._handle_response(
            requests.post(url, json=data, headers=self._build_headers()))

    def _delete(self, url, data):
        return self._handle_response(
            requests.delete(url, json=data, headers=self._build_headers()))

    def _build_headers(self):
        headers = {'x-api-key': self.api_key}
        return headers

    @staticmethod
    def _validate_key(api_key):
        if not api_key or type(api_key) is not str:
            raise ValueError('Invalid api ley \'%s\'' % api_key)

    @staticmethod
    def _handle_response(response):
        return response.json()
