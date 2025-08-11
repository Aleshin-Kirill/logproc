import pytest
from src.argument_parser import ArgumentParser
from unittest.mock import patch
from datetime import datetime


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # Тест с файлом и корректным report и без даты
        (
            ["--file", "file1.log", "--report", "average"],
            {"file": ["file1.log"], "report": "average"},
        ),
        # Тест с несколькими файлами и корректным report без даты
        (
            ["--file", "file1.log", "file2.log", "--report", "average"],
            {"file": ["file1.log", "file2.log"], "report": "average"},
        ),
        # Тест с файлом и корректным report и с датой
        (
            ["--file", "file1.log", "--report", "average", "--date", "2025-22-06"],
            {
                "file": ["file1.log"],
                "report": "average",
                "date": datetime.strptime("2025-22-06", "%Y-%d-%m").date(),
            },
        ),
    ],
)
def test_parse_args_valid_input(test_input, expected):
    with patch("sys.argv", ["script_name"] + test_input):
        args = ArgumentParser.parse_args()
        assert args.file == expected["file"]
        assert args.report == expected["report"]
        if args.date is not None:
            assert args.date == expected["date"]


@pytest.mark.parametrize(
    "invalid_input",
    [
        ["--report", "invalid_value"],  # Недопустимое значение для report
        ["--file"],  # Не указаны файлы
        ["--report"],  # Не указан
        # Тест с несколькими файлами и не корректным report
        ["--file", "file1.log", "file2.log", "--report", "invalid_value"],
        # Тест с файлом и не корректным report
        ["--file", "file1.log", "--report", "invalid_value"],
        # Тест с файлом и корректным report и не корректной датой
        ["--file", "file1.log", "--report", "average", "--date", "2025-06-22"],
    ],
)
def test_parse_args_invalid_input(invalid_input):
    with patch("sys.argv", ["script_name"] + invalid_input):
        with pytest.raises(SystemExit):  # argparse вызовет sys.exit() при ошибке
            ArgumentParser.parse_args()
