import pandas as pd


def analyze_data():

    file_path = "logs/sensor_data.csv"

    df = pd.read_csv(file_path)

    total = len(df)

    pass_count = (df["Result"] == "PASS").sum()
    fail_count = (df["Result"] == "FAIL").sum()

    pass_rate = (pass_count / total) * 100

    average_voltage = df["Voltage"].mean()
    average_temperature = df["Temperature"].mean()

    print("\n=== Hardware Validation Report ===")

    print(f"Total Tests: {total}")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"PASS Rate: {pass_rate:.1f}%")

    print(f"Average Voltage: {average_voltage:.2f} V")
    print(f"Average Temperature: {average_temperature:.2f} °C")


if __name__ == "__main__":
    analyze_data()