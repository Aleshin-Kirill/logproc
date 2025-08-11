import enum
from config import AVERAGE_REPORT_HEADERS


class ReportType:
    def __init__(self, name, headers):
        self.name = name
        self.headers = headers


class ReportTypes(enum.Enum):
    AVERAGE = "average"

    @classmethod
    def from_name(cls, name: str):
        try:
            return cls[name.upper()]
        except KeyError:
            return None


class ReportTypeFactory:
    @classmethod
    def get_report_type(cls, report_type: ReportTypes) -> ReportType | None:
        match report_type:
            case ReportTypes.AVERAGE:
                return ReportType("average", AVERAGE_REPORT_HEADERS.values())
            case _:
                return None
