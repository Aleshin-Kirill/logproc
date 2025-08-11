import pytest

from src.log_file_reader import LogFileReader
from src.log import Log
import os

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture()
def path_fixture(request):
    result = []
    for item in request.param:
        filename = item
        result.append(os.path.join(TESTDATA_DIRECTORY, filename))
    return result


@pytest.mark.parametrize(
    "path_fixture, expected",
    [(["example1.log"], {"len": 100}), (["example1.log", "example1.log"], {"len": 200})],
    indirect=["path_fixture"],
)
def test_load_logs(path_fixture, expected):
    logs = LogFileReader.load_logs(path_fixture)
    assert len(logs) == expected["len"]
    for log in logs:
        assert isinstance(log, Log)


@pytest.mark.parametrize(
    "path_fixture",
    [(["FileNotFound.log"]), (["example1.log", "FileNotFound.log"])],
    indirect=["path_fixture"],
)
def test_load_logs_file_not_found(path_fixture):
    with pytest.raises(FileNotFoundError):
        LogFileReader.load_logs(path_fixture)


@pytest.mark.parametrize(
    "path_fixture",
    [(["example1ErNoJson.log"]), (["example1.log", "example1ErNoJson.log"])],
    indirect=["path_fixture"],
)
def test_load_logs_file_json_invalid_deco(path_fixture):
    with pytest.raises(ValueError):
        LogFileReader.load_logs(path_fixture)
