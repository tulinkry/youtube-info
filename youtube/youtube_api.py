import logging

import requests

from .exception import ApiException

logger = logging.getLogger(__name__)


class YoutubeApi:
    """
    Facade implementing method for data from youtube api.
    """

    def __init__(self,
                 base_url='https://www.googleapis.com/youtube/v3/',
                 apikey=None,
                 session=None):
        """
        Construct a new session object for querying youtube api v3
        about generic information.

        :param base_url the base url for this api
        :param apikey: api key for youtube api v3
        :param session: optional requests session to use for accessing the api
        """
        self._session = session or requests.sessions.session()
        self._session.headers.update({
            'accept': 'application/json'
        })
        self._apikey = apikey
        self._base_url = base_url

        if not self._apikey:
            raise Exception('api key is None')

        if not self._base_url:
            raise Exception('base url is None')

    def get(self, **kwargs):
        """
        Call the youtube api via requests library. The kwargs are enriched with
        api key and the pagination itself is handled
        automatically by this method.

        :param kwargs: optional arguments for requests.get method
        :return: yields the paginated responses one by one
        """
        kwargs.setdefault('params', {}).update({
            'key': self._apikey,
            'maxResults': 50,
        })

        while True:
            logger.info('fetching the url %s?%s', self._base_url, '&'.join(
                map(lambda param: '='.join(map(str, param)),
                    kwargs['params'].items())))

            response = self._session.get(self._base_url, **kwargs)

            if response.status_code != 200:
                try:
                    parsedResponse = response.json()
                    if 'error' in parsedResponse and \
                            'errors' in parsedResponse['error']:
                        raise ApiException('API call failed with {}: {}'.format(
                            response.status_code,
                            ' and '.join(map(
                                lambda error: '{}: {}'.format(
                                    error.get('domain', ''),
                                    error.get('reason', '')),
                                parsedResponse['error']['errors']))
                        ))
                    raise ApiException(
                        'API call failed with unknown error: {} {}'.format(
                            response.status_code, response.text))
                except ValueError as e:
                    # unable to parse json
                    raise ApiException(e)

            parsedResponse = response.json()
            yield parsedResponse

            if 'nextPageToken' not in parsedResponse:
                break

            kwargs['params'].update({
                'pageToken': parsedResponse['nextPageToken']
            })

    def __enter__(self):
        self._session.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.__exit__(exc_type, exc_val, exc_tb)


if __name__ == '__main__':
    raise Exception("This module is not runable.")
