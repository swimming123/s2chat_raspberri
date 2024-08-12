라즈베리파이 git
리눅스 캡처

심박센서 GPIO 선
git clone https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor 

라즈베리파이 GPIO

카메라
https://blog.naver.com/PostView.naver?blogId=rlrkcka&logNo=223526527117&parentCategoryNo=&categoryNo=34&viewDate=&isShowPopularPosts=false&from=postView

회로
https://tutorials-raspberrypi.com/raspberry-pi-heartbeat-pulse-measuring/
https://m.blog.naver.com/siryua/221232071978
https://blog.naver.com/PostView.nhn?blogId=intopion&logNo=222009832752


https://blog.naver.com/simjk98/221873207244
https://blog.naver.com/osning38/223450327614
https://blog.naver.com/simjk98/221220087802
https://github.com/tutRPi/Raspberry-Pi-Heartbeat-Pulse-Sensor



연결 방법
GND 3.3 SIGNAL

GND 핀을 라즈베리파이의 GND 핀에 연결합니다.
3.3V 핀을 라즈베리파이의 3.3V 핀에 연결합니다.
SIGNAL 핀을 라즈베리파이의 특정 GPIO 핀 (예: GPIO17) 에 연결합니다.




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
    while True:
        sensor_value = read_sensor()
        print(f"센서 값: {sensor_value}")
        time.sleep(0.01)  # 10ms 간격으로 데이터 수집

except KeyboardInterrupt:
    print("데이터 수집을 종료합니다.")

finally:
    GPIO.cleanup()
