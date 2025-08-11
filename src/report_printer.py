from tabulate import tabulate


class ReportPrinter:
    @staticmethod
    def print_cmd_table(report):
        print(tabulate(report, headers="keys"))
