import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

bus = smbus.SMBus(1)
address = 0x48
bus.write_byte_data(address, 0x01, 0x64)
bus.write_i2c_block_data(address, 0x02, [0x18, 0x00])
bus.write_i2c_block_data(address, 0x03, [0x19, 0x00])

def readInt():
  read1 = bus.read_i2c_block_data(address, 0)
  return read1[0]

def readBin():
  read2 = bus.read_i2c_block_data(address, 0)
  return format(read2[1], '08b')

def binarify():
  bin = readBin()
  bin = map(int, bin)
  con = 0
  count = 0
  for i in bin:
    count = count - 1
    con = con + i*(2**count)
  return round(con,1)

while True:
  value = readInt() + binarify()
  if (GPIO.input(11) == True):
    GPIO.output(7, True)
    GPIO.output(18, False)
    print('Temperature: ' + str(value) + ' C (AC on)')
  else:
    GPIO.output(18, True)
    GPIO.output(7, False)
    print('Temperature ' + str(value) + ' C (AC off)')
  time.sleep(1)
