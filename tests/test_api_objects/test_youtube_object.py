import pytest

from youtube import YoutubeVideoInfo


def test_basic_object():
    video = YoutubeVideoInfo({'id': 10, 'text': 'text'})
    assert video is not None
    assert video.id == 10
    assert video.text == 'text'


@pytest.mark.parametrize(
    ('name'),
    [
        ('nothing'),
        ('body'),
        ('json')
    ]
)
def test_invalid_attributes(name):
    video = YoutubeVideoInfo({'id': 10, 'text': 'text'})
    with pytest.raises(AttributeError):
        getattr(video, name)
