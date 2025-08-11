import json


class Log:
    def __init__(self, timestamp, status, url, request_method, response_time, http_user_agent):
        self.timestamp = timestamp
        self.status = status
        self.url = url
        self.request_method = request_method
        self.response_time = response_time
        self.http_user_agent = http_user_agent

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(
            timestamp=data["@timestamp"],
            status=data["status"],
            url=data["url"],
            request_method=data["request_method"],
            response_time=data["response_time"],
            http_user_agent=data["http_user_agent"],
        )

    def __eq__(self, other):
        if isinstance(other, Log):
            if self.timestamp != other.timestamp:
                return False
            elif self.status != other.status:
                return False
            elif self.url != other.url:
                return False
            elif self.request_method != other.request_method:
                return False
            elif self.response_time != other.response_time:
                return False
            elif self.http_user_agent != other.http_user_agent:
                return False
            else:
                return True
        return False
