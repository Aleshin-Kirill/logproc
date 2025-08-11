from src.argument_parser import ArgumentParser
from src.log_file_reader import LogFileReader
from src.report_generator import ReportGenerator
from src.report_printer import ReportPrinter
from src.report import ReportTypes, ReportTypeFactory
from src.logs_filter import LogsFilter

if __name__ == "__main__":
    args = ArgumentParser.parse_args()
    logs = LogFileReader.load_logs(args.file)

    # sort
    if args.date is not None:
        logs = LogsFilter.filter_logs_by_date_equals(logs, args.date)

    # report
    report_type = ReportTypeFactory.get_report_type(ReportTypes.from_name(args.report))
    report = ReportGenerator.make(report_type, logs)

    ReportPrinter.print_cmd_table(report)
