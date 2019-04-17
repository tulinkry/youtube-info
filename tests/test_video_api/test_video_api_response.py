def test_single_id(api):
    with api as videos:
        items = list(videos.info('oT3mCybbhf0'))

        assert len(items) == 1
        assert items[0].id == 'oT3mCybbhf0'
        assert items[0].snippet.title == 'AVICII & RICK ASTLEY - ' \
                                         'Never Gonna Wake You Up ' \
                                         '(NilsOfficial Mashup)'


def test_multiple_ids(api):
    with api as videos:
        items = list(videos.info('oT3mCybbhf0', 'sgBZVLr91ug'))

        assert len(items) == 2
        assert items[0].id == 'oT3mCybbhf0'
        assert items[0].snippet.title == 'AVICII & RICK ASTLEY - ' \
                                         'Never Gonna Wake You Up ' \
                                         '(NilsOfficial Mashup)'

        assert items[1].id == 'sgBZVLr91ug'
        assert items[1].snippet.title == 'Karol G - Punto G'
