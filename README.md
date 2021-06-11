# IOT Final Project: Gesture Control
## Demo Video
* https://www.youtube.com/watch?v=M3KnmwjnczY
---
## Precondition (Important!)
* Make sure that your Raspberry PI has already set up. In the Project, we don’t teach how to do that.
* Also, you can see the “RPI_INSTALL_DOC.pdf” in the project. That will teach you step-by-step process to set up your Raspberry PI.
---
## Overview
* This is a magic gloves! You can only use it with corresponding gesture to control all your furniture like music player, fan, air conditioner, robot car…… In this, I use the Robot Car to demonstrate.
* This Project is for something that you usually do in your life but you need to take some effort to do, just like open the light, close the air conditioner, lock your door…… But if you have the magic glove, you will not need to stand up, go ahead to your light, remote control or something what you use to control your target, you just need to make some gesture toward your target and then everything is wonderful!
---
## Technologies involved
1.	The MPU6050 module which including the “Accelerometer” and “Gyroscope” can use to detect out hand gesture.
2.	Using the python’s “smbus” package to address the MPU6050 data, let us know what gesture we are making.
3.	After getting the gesture’s data, we simply use the Bluetooth, WIFI or RF signal to transmit the data to our Raspberry PI. For this project, we use the Bluetooth.
4.	Address the data to make out item do something what we want.
5.	Return some data of our item and display on our screen to detect.
---
## Component
#### For hand gesture sensor (Sender):
1.	MPU6050 module or simply an Accelerometer
2.	Raspberry PI Zero which include the Bluetooth module. (You also can use something that can transmit data from your sender to your receiver)
3.	Gloves or something set the MPU6050 and PRI Zero
4.	double-sided tape to stick your item to your gloves.
5.	Power (Maybe a battery or Mobile power) for your RPI Zero

#### For hand gesture handler (Receiver):
1.	Robot Car or something you want to control
2.	Raspberry PI 3 which include the Bluetooth module (Or something you can receive your data from sender)
3.	Power (Maybe a battery or Mobile power) for your Raspberry PI 3
---
## Technologies implementation
## MPU6050 module:
MPU6050 use the I2C interface, so we need to make our raspberry pi enable the I2C interface function.

**Part 1: Configure the RPI I2C**
1.	Open the configuration interface
* In your terminal, input the “sudo raspi-config”
2.	Select Interfacing Configurations
* ![](https://i.imgur.com/FnpoUdr.png)
3.	Select -> I2C
* ![](https://i.imgur.com/mQqfpCs.png)
4.	Enable I2C configuration by press “Yes”
* ![](https://i.imgur.com/cMiq4kp.png)
Then you can see the picture
![](https://i.imgur.com/5fMu519.png)
5.  Finally, Select Yes if it asks to Reboot or you can reboot your RPI by yourself.
* After booting raspberry Pi, we can check user-mode I2C port by entering following command.
![](https://i.imgur.com/9ZjRun6.png)

**Part 2: Scan and Test the I2C on RPI**
1.	get i2c tools by using apt package manager
* sudo apt-get install -y i2c-tools
2.	connect you I2C device to your RPI
* ![](https://i.imgur.com/a3NH8zg.png) like this “MPU6050”
3.	scan the port using following command
* sudo i2cdetect -y 1
if success, your will see like this:
![](https://i.imgur.com/WStJgir.png)
---
## Bluetooth module:
We will use the python for control the Bluetooth communication. In the part, you will install the python Bluetooth package and program the python code to control the Bluetooth to transmit data from sender to receiver.

**Part 1: Install python-bluezthat for your RPI**
1.	sudo apt-get install python-bluez
* In some condition, you may need to add the command
    * sudo apt-get install libbluetooth-dev libbluetooth3
2.	write a python code that contain the “import Bluetooth”
* this is to check if you install the package successfully

**Part 2: Install “smbus” package for MPU6050 to address the data.**
1.  pip3 install smbus
* If you have already the package, just skip it.
2.	write a python code that contain the “import smbus”
* this is to check if you install the package successfully

**Part 3: Write two code, one for sender and one for receiver**
1.	For sender
* You can get the code by name "client.py" in the project
2.	For Receiver
* You can get the code by name “server.py” in the project
3.	If you want to test the Bluetooth programming
* Reference: https://shengyu7697.github.io/blog/2019/09/11/%E5%9C%A8-RPi3-%E4%B8%8A%E5%AF%AB%E7%AC%AC%E4%B8%80%E6%94%AF%E8%97%8D%E8%8A%BD%E7%A8%8B%E5%BC%8F-Python/
---
## Robot Car:
**Part 1: Configure all components of your car**
* ![](https://i.imgur.com/DBJMN9t.png)
* ![](https://i.imgur.com/coFWCS2.png)
* ![](https://i.imgur.com/Cms9lsP.png)
* ![](https://i.imgur.com/1zAq77B.png)
* ![](https://i.imgur.com/fGCcqMS.png)

**Part 2: Configure the L298N motor controller**
* This is for logically control you Robot car. L298N contain the four output controlled by Raspberry PI’s GPIO and 2 port for power input.
* ![](https://i.imgur.com/Z9eKFJJ.png)
* ![](https://i.imgur.com/1D9PPFw.png)
---

## Code implementation
#### client.py
* In the part, you will learn how to get the MPU6050’data and using the smbus package to address it. Finally transmit it to your target.

**Part 1: set up the MPU6050**
* ![](https://i.imgur.com/hbXDWLq.png)
    * Basic parameter set up.
* ![](https://i.imgur.com/UnaUjjy.png)
    * Initialize the MPU6050
    * 
**Part 2: Address the MPU6050 data**
* ![](https://i.imgur.com/4YJcAfX.png)
    * Get the MPU6050’s data
* ![](https://i.imgur.com/ILJ5aUG.png)
    * Make the data easy to read

**Part 3: Transmit the data to your receiver**
* ![](https://i.imgur.com/t7Q7OhE.png)
    * getDirection: transform the MPU6050’s data to the direction
    * if the direction change, send to data
---
#### server.py
* In the part, you will learn how to get the data from your sender by bluetooth and using the RPi.GPIO package to address it. Finally make your car move!

**Part 1: set up the GPIO PIN**
* ![](https://i.imgur.com/LFiKKqt.png)
* ![](https://i.imgur.com/gnwNWKC.png)

**Part 2: make your Bluetooth to accept status**
* ![](https://i.imgur.com/9s7bKYJ.png)

**Part 3: address the data from your sender, and do the corresponding action**
* ![](https://i.imgur.com/OeXWqWM.png)
---
## Reference Document:
* https://rootsaid.com/spinelcrux-gesture-controlled-robot-1/	
* https://www.eprice.com.tw/mobile/talk/4523/5385251/1/rv/samsung-review/
* https://www.youtube.com/watch?v=Xz0gZCVxGnw
* https://circuitdigest.com/microcontroller-projects/mpu6050-gyro-sensor-interfacing-with-raspberry-pi
* https://shengyu7697.github.io/blog/2018/02/06/Bluetooth-Programming/
* https://medium.com/@kalpeshnpatil/raspberry-pi-interfacing-with-mpu6050-motion-sensor-c9608cd5f59c
















