import pytest
from src.report import ReportType, ReportTypeFactory, ReportTypes
from src.log_file_reader import LogFileReader
import os
from src.report_generator import ReportGenerator

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), "data")


@pytest.mark.parametrize(
    "report_type, logs, expected",
    [
        (
            ReportTypeFactory.get_report_type(ReportTypes.AVERAGE),
            LogFileReader.load_logs([os.path.join(TESTDATA_DIRECTORY, "example1.log")]),
            [
                {"avg_response_time": 0.043, "handler": "/api/context/...", "total": 21},
                {
                    "avg_response_time": 0.158,
                    "handler": "/api/homeworks/...",
                    "total": 71,
                },
                {
                    "avg_response_time": 0.035,
                    "handler": "/api/specializations/...",
                    "total": 6,
                },
                {"avg_response_time": 0.072, "handler": "/api/users/...", "total": 1},
                {
                    "avg_response_time": 0.056,
                    "handler": "/api/challenges/...",
                    "total": 1,
                },
            ],
        ),
    ],
)
def test_make(report_type, logs, expected):
    report = ReportGenerator.make(report_type, logs)
    assert report == expected
