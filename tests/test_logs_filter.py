import pytest
import os
from src.logs_filter import LogsFilter
from src.log_file_reader import LogFileReader
from datetime import datetime

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "data")


@pytest.mark.parametrize(
    "logs, value_date, expected_len",
    [
        (
            LogFileReader.load_logs([os.path.join(TESTDATA_DIRECTORY, "example1.log")]),
            datetime.strptime("2025-22-06", "%Y-%d-%m").date(),
            100,
        ),
        (
            LogFileReader.load_logs([os.path.join(TESTDATA_DIRECTORY, "example2.log")]),
            datetime.strptime("2025-22-06", "%Y-%d-%m").date(),
            6757,
        ),
    ],
)
def test_filter_logs_by_date_equals(logs, value_date, expected_len):
    filter_logs = LogsFilter.filter_logs_by_date_equals(logs, value_date)
    assert len(filter_logs) == expected_len
