from face_detector.utils import parse_source


def test_parse_source_numeric():
    assert parse_source('0') == 0
    assert parse_source('12') == 12


def test_parse_source_non_numeric():
    assert parse_source('video.mp4') == 'video.mp4'
    assert parse_source('rtsp://example') == 'rtsp://example'
