import argparse
from src.report import ReportTypes
from datetime import datetime


class ArgumentParser:
    parser = argparse.ArgumentParser(description="Processing the log file")
    parser.add_argument("--file", type=str, nargs="+", help="file path")
    parser.add_argument(
        "--report", type=str, choices=[e.value for e in ReportTypes], help="report name"
    )
    parser.add_argument(
        "--date",
        type=lambda s: datetime.strptime(s, "%Y-%d-%m").date(),
        required=False,
        help="report by date",
    )

    @classmethod
    def parse_args(cls):
        return cls.parser.parse_args()
