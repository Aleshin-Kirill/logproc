import json
from src.log import Log


class LogFileReader:

    @staticmethod
    def load_logs(files_paths: list[str]) -> list[Log]:
        logs = []
        for file_path in files_paths:
            try:
                with open(file_path, "r") as file:
                    logs.extend([Log.from_json(line) for line in file])
            except FileNotFoundError:
                raise FileNotFoundError(f"File {file_path} not found")
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON format in file {file_path}")
        return logs
