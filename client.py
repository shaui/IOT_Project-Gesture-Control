import bluetooth
import smbus            #import SMBus module of I2C
from time import sleep          #import

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value

def getDirection(x,y,z):
    if(y >= 0.3):
        return "forward"
    elif(y <= -0.3):
        return "backward"
    elif(x >= 0.3):
        return "right"
    elif(x <= -0.3):
        return "left"
    else:
        return "stop"

def changeDirection(newD, direction):
    return (newD != direction)

def main():
    bd_addr = "B8:27:EB:8F:ED:40"

    port = 1

    MPU_Init()

    print (" Reading Data of Gyroscope and Accelerometer")

    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    #get the intial direction
    direction = "stop"
    while True:
        try:
            print("now:" + direction)
            
            #Read Accelerometer raw value
            acc_x = read_raw_data(ACCEL_XOUT_H)
            acc_y = read_raw_data(ACCEL_YOUT_H)
            acc_z = read_raw_data(ACCEL_ZOUT_H)
            
            #Read Gyroscope raw value
            gyro_x = read_raw_data(GYRO_XOUT_H)
            gyro_y = read_raw_data(GYRO_YOUT_H)
            gyro_z = read_raw_data(GYRO_ZOUT_H)
            
            #Full scale range +/- 250 degree/C as per sensitivity scale factor
            Ax = acc_x/16384.0
            Ay = acc_y/16384.0
            Az = acc_z/16384.0
            
            Gx = gyro_x/131.0
            Gy = gyro_y/131.0
            Gz = gyro_z/131.0
            
            #get the new Direction
            newD = getDirection(Ax, Ay, Az)
            if(changeDirection(newD, direction)):
                direction = newD
                sock.send(direction)
                print("change to:" + direction)
            #sock.send(msg)
            #print(msg)
            sleep(0.1)
        except KeyboardInterrupt as kie:
            print("KeyboardInterrupt")
            break;
        
        except Exception as e:
            print("Exception")
            break;
        
    sock.close()
    
main()


            
        
