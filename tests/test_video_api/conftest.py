import configparser
import os

import betamax
import pytest

from youtube import YoutubeVideosApi


def get_config(f):
    config = configparser.ConfigParser()
    config.read(f)

    return config['youtube']['apikey']


with betamax.Betamax.configure() as config:
    if 'AUTH_FILE' in os.environ:
        # If the tests are invoked with an AUTH_FILE environ variable
        API_KEY = get_config(os.environ['AUTH_FILE'])
        # Always re-record the cassetes
        # https://betamax.readthedocs.io/en/latest/record_modes.html
        config.default_cassette_options['record_mode'] = 'all'
    else:
        API_KEY = 'false_token'
        # Do not attempt to record sessions with bad fake token
        config.default_cassette_options['record_mode'] = 'none'

    # Hide the token in the cassettes
    config.define_cassette_placeholder('<API_KEY>', API_KEY)


@pytest.fixture
def api(betamax_session):
    return YoutubeVideosApi(API_KEY, betamax_session)
