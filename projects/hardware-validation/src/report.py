import pandas as pd
from datetime import datetime


def generate_report():

    df = pd.read_csv("logs/sensor_data.csv")

    total = len(df)
    pass_count = (df["Result"] == "PASS").sum()
    fail_count = (df["Result"] == "FAIL").sum()

    pass_rate = pass_count / total * 100

    average_voltage = df["Voltage"].mean()
    average_temperature = df["Temperature"].mean()

    report = f"""
========================================
       HARDWARE VALIDATION REPORT
========================================

Test Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

[TEST SUMMARY]

Total Tests : {total}
PASS        : {pass_count}
FAIL        : {fail_count}
PASS Rate   : {pass_rate:.1f}%

[MEASUREMENT SUMMARY]

Average Voltage     : {average_voltage:.2f} V
Average Temperature : {average_temperature:.2f} C

[FINAL RESULT]

{"PASS" if fail_count == 0 else "FAIL"}

========================================
"""

    with open(
        "reports/validation_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    print(report)
    print("Report saved successfully!")


if __name__ == "__main__":
    generate_report()