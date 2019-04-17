import logging

from .exception import ApiException
from .youtube_api import YoutubeApi
from .youtube_video_info import YoutubeVideoInfo

logger = logging.getLogger(__name__)


class YoutubeVideosApi(YoutubeApi):
    """
    Videos facade implementing method for obtaining information about videos
    from youtube.
    """

    def __init__(self, apikey, session=None):
        """
        Construct a new session object for querying youtube api v3
        about video information.

        :param apikey: api key for youtube api v3
        :param session: optional requests session to use for accessing the api
        """
        super().__init__('https://www.googleapis.com/youtube/v3/videos',
                         apikey, session=session)

    def info(self, *video_ids, **kwargs):
        logger.debug('looking for videos with ids: %s', ', '.join(video_ids))

        kwargs.setdefault('params', {}).update({
            'id': ','.join(video_ids),
            # 'chart': 'mostPopular',
            'part': ','.join(['snippet', 'statistics'])
        })

        gotAny = False
        for response in self.get(**kwargs):
            if 'items' not in response:
                logger.warning('items are not contained in the response')
                continue

            for item in response['items']:
                gotAny = True
                video = YoutubeVideoInfo(item)
                logger.debug('found video details for id = %s', video.id)
                yield video

        if not gotAny:
            raise ApiException('No items found in the responses, bad format?')


if __name__ == '__main__':
    raise Exception("This module is not runable.")
