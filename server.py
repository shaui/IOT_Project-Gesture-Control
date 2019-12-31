import bluetooth
import RPi.GPIO as GPIO
import time

pin_right_f = 17
pin_right_b = 27
pin_left_f = 22
pin_left_b = 10

def forward():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.HIGH)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.HIGH)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("forward!")

def backward():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.HIGH)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.HIGH)
    print("backward!")

def left():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.HIGH)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.HIGH)
    print("left!")

def right():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.HIGH)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.HIGH)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("right!")

def stop():
    # set the BCM17 pin to have the current
    GPIO.output(pin_right_f, GPIO.LOW)
    # set the BCM27 pin to have the current
    GPIO.output(pin_right_b, GPIO.LOW)
    # set the BCM22 pin to have the current
    GPIO.output(pin_left_f, GPIO.LOW)
    # set the BCM10 pin to have the current
    GPIO.output(pin_left_b, GPIO.LOW)
    print("stop!")

def closeGPIO(gpio_pin):
    for i in gpio_pin:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()

def main():
    # set the pin mode to BCM
    GPIO.setmode(GPIO.BCM)
    gpio_pin = [pin_right_f, pin_right_b, pin_left_f, pin_left_b]
    for i in gpio_pin:
        GPIO.setup(i, GPIO.OUT)
   
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    port = 1
    server_sock.bind(("",port))
    server_sock.listen(1)

    client_sock,address = server_sock.accept()
    print ("Accepted connection from ",address)
    while True:
        try:
            byteData = client_sock.recv(1024)
            data = str(byteData)[1:].strip("'")
            #print (data)
            if(data == "forward"):
                forward()
            elif(data == "backward"):
                backward()
            elif(data == "right"):
                right()
            elif(data == "left"):
                left()
            elif(data == "stop"):
                stop()
            else:
                print("unknoen message")
        except KeyboardInterrupt as kie:
            print("KeyboardInterrupt")
            break;
        except Exception as e:
            print("Exception")
            break
    
    closeGPIO(gpio_pin)  
    client_sock.close()
    server_sock.close()
    
if __name__ == '__main__':
    main()
