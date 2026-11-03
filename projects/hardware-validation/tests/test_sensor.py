from src.main import validate_sensor


def test_normal_sensor():
    result, error = validate_sensor(3.8, 30.0)

    assert result == "PASS"
    assert error == "Normal"


def test_low_voltage():
    result, error = validate_sensor(3.0, 30.0)

    assert result == "FAIL"
    assert "Voltage out of range" in error


def test_high_voltage():
    result, error = validate_sensor(4.3, 30.0)

    assert result == "FAIL"
    assert "Voltage out of range" in error


def test_high_temperature():
    result, error = validate_sensor(3.8, 50.0)

    assert result == "FAIL"
    assert "Temperature out of range" in error


def test_both_sensor_errors():
    result, error = validate_sensor(3.0, 50.0)

    assert result == "FAIL"
    assert "Voltage out of range" in error
    assert "Temperature out of range" in error