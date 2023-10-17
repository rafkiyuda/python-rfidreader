import serial

# Tentukan port serial yang digunakan oleh RFID reader
serial_port = "COM3"  # Gantilah dengan port yang sesuai

try:
    ser = serial.Serial(
        serial_port, 9600
    )  # 9600 adalah kecepatan baud umum, sesuaikan jika diperlukan
    while True:
        data = ser.readline().strip()
        print(f"Data RFID: {data.decode('utf-8')}")
except KeyboardInterrupt:
    ser.close()
