from collections import defaultdict
from src.report import ReportType, ReportTypes
from src.log_file_reader import Log
from config import AVG_PRECISION
from config import AVERAGE_REPORT_HEADERS


class ReportGenerator:

    @staticmethod
    def make(report_type: ReportType, logs: list[Log]):
        match report_type.name:
            case ReportTypes.AVERAGE.value:
                return ReportGenerator.__generate_average_report(logs, report_type.headers)
            case _:
                return None

    @staticmethod
    def __generate_average_report(logs: list[Log], headers: list[str]):
        endpoint_stats = defaultdict(lambda: {"count": 0, "total_time": 0.0})
        for log in logs:
            if log.url and log.response_time is not None:
                endpoint_stats[log.url]["count"] += 1
                endpoint_stats[log.url]["total_time"] += log.response_time

        report = []

        for endpoint, stats in endpoint_stats.items():
            avg_time = stats["total_time"] / stats["count"] if stats["count"] > 0 else 0
            temp = dict.fromkeys(headers)
            temp[AVERAGE_REPORT_HEADERS.get("handler")] = endpoint
            temp[AVERAGE_REPORT_HEADERS.get("total")] = stats["count"]
            temp[AVERAGE_REPORT_HEADERS.get("avg_response_time")] = round(avg_time, AVG_PRECISION)
            report.append(temp)
        return report
