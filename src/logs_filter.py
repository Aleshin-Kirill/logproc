from datetime import datetime, date
from src.log import Log


class LogsFilter:

    @staticmethod
    def filter_logs_by_date_equals(logs: list[Log], value_date: date) -> list[Log]:
        return list(
            filter(lambda x: datetime.fromisoformat(x.timestamp).date() == value_date, logs)
        )
