import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
SIGNAL_PIN = 17  # SIGNAL 핀에 연결된 GPIO 번호

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SIGNAL_PIN, GPIO.IN)

# 센서 데이터 읽기 함수
def read_sensor():
    return GPIO.input(SIGNAL_PIN)

# 데이터 수집
try:
    print("센서 데이터를 수집합니다. (Ctrl+C로 종료)")
    for _ in range(1000):  # 1000번 데이터 수집
        sensor_value = read_sensor()
        print(f"센서 값: {sensor_value}")
        time.sleep(0.01)  # 10ms 간격으로 데이터 수집

except KeyboardInterrupt:
    print("데이터 수집을 종료합니다.")

finally:
    GPIO.cleanup()