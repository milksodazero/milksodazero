import pandas as pd
import matplotlib.pyplot as plt


def visualize_data():

    # CSV 데이터 불러오기
    df = pd.read_csv("logs/sensor_data.csv")

    # 측정 순서
    x = range(1, len(df) + 1)

    # 그래프 영역 생성
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    # 전압 그래프
    axes[0].plot(x, df["Voltage"], marker="o")
    axes[0].axhline(y=3.3, linestyle="--", label="Minimum Voltage")
    axes[0].axhline(y=4.2, linestyle="--", label="Maximum Voltage")

    axes[0].set_title("Battery Voltage Monitoring")
    axes[0].set_ylabel("Voltage (V)")
    axes[0].legend()
    axes[0].grid(True)

    # 온도 그래프
    axes[1].plot(x, df["Temperature"], marker="o")
    axes[1].axhline(y=20, linestyle="--", label="Minimum Temperature")
    axes[1].axhline(y=45, linestyle="--", label="Maximum Temperature")

    axes[1].set_title("Battery Temperature Monitoring")
    axes[1].set_xlabel("Measurement Number")
    axes[1].set_ylabel("Temperature (°C)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()

    # 그래프 저장
    plt.savefig("reports/sensor_analysis.png")

    # 그래프 화면 표시
    plt.show()


if __name__ == "__main__":
    visualize_data()