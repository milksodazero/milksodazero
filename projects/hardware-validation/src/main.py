import random
import time
import csv
from datetime import datetime


# 센서 정상 범위
MIN_VOLTAGE = 3.3
MAX_VOLTAGE = 4.2

MIN_TEMPERATURE = 20.0
MAX_TEMPERATURE = 45.0


def read_voltage():
    return round(random.uniform(3.0, 4.2), 2)


def read_temperature():
    return round(random.uniform(20.0, 50.0), 1)


def validate_sensor(voltage, temperature):
    errors = []

    if not MIN_VOLTAGE <= voltage <= MAX_VOLTAGE:
        errors.append("Voltage out of range")

    if not MIN_TEMPERATURE <= temperature <= MAX_TEMPERATURE:
        errors.append("Temperature out of range")

    if errors:
        return "FAIL", ", ".join(errors)

    return "PASS", "Normal"


def save_data(data):
    file_path = "logs/sensor_data.csv"

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Timestamp",
                "Voltage",
                "Temperature",
                "Result",
                "Error"
            ])

        writer.writerow(data)


def main():
    print("=== Hardware Validation System ===")

    for i in range(10):
        voltage = read_voltage()
        temperature = read_temperature()

        result, error = validate_sensor(voltage, temperature)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(
            f"[{i + 1}] "
            f"Voltage: {voltage} V | "
            f"Temperature: {temperature} °C | "
            f"Result: {result}"
        )

        if result == "FAIL":
            print(f"    Error: {error}")

        save_data([
            timestamp,
            voltage,
            temperature,
            result,
            error
        ])

        time.sleep(1)


if __name__ == "__main__":
    main()