import serial
import time


dev = serial.Serial('/dev/ttyACM0')
time.sleep(1)
dev.write(b'IDN\n')
answer = dev.readline()
print('The answer is {}'.format(answer))

dev.write(b'IN:CH0\n')
value = dev.readline()
print('The value is {}'.format(value))
dev.write(b'OUT:CH0:2900\n')
time.sleep(0.05)
dev.write(b'IN:CH0\n')
value = dev.readline()
print('The value is {}'.format(value))
dev.write(b'OUT:CH0:10\n')
time.sleep(0.05)
dev.write(b'IN:CH0\n')
value = dev.readline()
print('The value is {}'.format(value))