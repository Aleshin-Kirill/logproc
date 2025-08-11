import pytest
import json

from src.log import Log


@pytest.mark.parametrize(
    "json_log, expected_log",
    [
        (
            '{"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", '
            '"response_time": 0.024, "http_user_agent": "..."}',
            Log(
                timestamp="2025-06-22T13:57:32+00:00",
                status=200,
                url="/api/context/...",
                request_method="GET",
                response_time=0.024,
                http_user_agent="...",
            ),
        )
    ],
)
def test_from_json(json_log, expected_log):
    log = Log.from_json(json_log)
    assert log == expected_log


@pytest.mark.parametrize(
    "json_log",
    [
        '"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", '
        '"response_time": 0.024, "http_user_agent": "..."',
    ],
)
def test_from_json_invalid(json_log):
    with pytest.raises(json.JSONDecodeError):
        log = Log.from_json(json_log)
