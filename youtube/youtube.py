import configparser
import csv
import logging
import os
import sys

import click

from .exception import ApiException
from .youtube_videos_api import YoutubeVideosApi

logger = logging.getLogger('youtube')


def validate_config(_, __, value):
    """
    Validate the configuration option from command line.
    :param _: context
    :param __: parameter name
    :param value: path to the configuration file
    :return: parsed configuration as a dict
    """
    if not os.path.exists(value):
        raise click.BadParameter('The configuration file does not exist')

    config = configparser.ConfigParser()
    if value not in config.read(value):
        raise click.BadParameter('Unable to parse the '
                                 'configuration file {}'.format(value))

    if 'youtube' not in config:
        raise click.BadParameter('The configuration file {} does not have a '
                                 '\'youtube\' section'.format(value))

    if 'apikey' not in config['youtube']:
        raise click.BadParameter('The configuration file {} does not have a '
                                 '\'apikey\' in the \'youtube\' '
                                 'section'.format(value))

    return config


@click.command()
@click.argument('id', nargs=-1, required=True)
@click.option('-c',
              '--config',
              'configuration',
              help='Configuration file with the youtube api token '
                   '(by default it looks in ~/.youtube.auth.cfg)',
              default=os.path.expanduser('~/.youtube.auth.cfg'),
              callback=validate_config)
@click.option('--debug', is_flag=True, default=False,
              help='print debugging information to stderr')
def main(id, configuration, debug):
    """
    Command line tool for querying details about youtube videos.

    <ID> ID of the video (can be repeated for more videos)

    The configuration file needs to have a youtube section with apikey in it:

    \b
    [youtube]
    apikey = xxx
    """
    logger.setLevel(logging.DEBUG if debug else logging.ERROR)
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(name)s -'
                               ' %(levelname)s - %(message)s')

    with YoutubeVideosApi(apikey=configuration['youtube']['apikey']) as videos:
        first = True
        writer = csv.writer(sys.stdout)
        try:
            for info in videos.info(*id):
                if first:
                    writer.writerow(['id', 'title', 'publishedAt', 'viewCount'])
                row = [
                    info.id,
                    info.snippet.title,
                    info.snippet.publishedAt,
                    info.statistics.viewCount
                ]

                logger.debug('writing result to stdout: %r', row)
                writer.writerow(row)
                first = False
        except ApiException as e:
            print(e, file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
