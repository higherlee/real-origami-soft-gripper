import time
from threading import Thread
import tkinter as tk
import spidev
import RPi.GPIO as GPIO
import time
from ina219 import INA219, DeviceRangeError
##### Settings for Grip Operation #####
key_motor_state ="0"
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
Motor_B_1= 9
Motor_B_2= 10
Relay_valve = [17,27]
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_B_1,GPIO.OUT)
GPIO.setup(Motor_B_2,GPIO.OUT)
GPIO.setup(Relay_valve,GPIO.OUT)
#######################################

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 2.0

ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS, address=0x40, busnum=1)
ina.configure(ina.RANGE_16V)


max_len = 15

for i in range(0,1):
    GPIO.setup(Relay_valve[i],GPIO.OUT)

Motor_B_1_PWM=GPIO.PWM(Motor_B_1,500)
Motor_B_2_PWM=GPIO.PWM(Motor_B_2,500)
Motor_B_1_PWM.start(0)
GPIO.output(Motor_B_1,False)
GPIO.output(Motor_B_2,True)

class ControlThread(Thread):
    def __init__(self, gui_update_callback):
        super().__init__()
        self.gui_update_callback = gui_update_callback
        ##### Init #####
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        GPIO.output(Motor_B_1,False)
        GPIO.output(Motor_B_2,False)
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)

        ################
    
    
    def gripOperation(self):
        self.gui_update_callback(0, "Processing...")
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        GPIO.output(Motor_B_1,True)
        GPIO.output(Motor_B_2,False)
        current_readings = []
        while True:
            try:
                bus_voltage = ina.voltage()
                current = ina.current()
                power = ina.power()
                shunt_voltage = ina.shunt_voltage()

                current_readings.append(current)

                if len(current_readings) > max_len:
                    current_readings.pop(0)

                if len(current_readings) == max_len:
                    moving_average = sum(current_readings) / len(current_readings)
                else:
                    moving_average = None

                print(f"Bus Voltage: {bus_voltage:.3f} V")
                print(f"Shunt Voltage: {shunt_voltage:.3f} mV")
                print(f"Current: {current:.3f} mA")
                if moving_average is not None:
                    print(f"Moving Average Current: {moving_average:.3f} mA")
                    self.gui_update_callback(abs(int(moving_average/4)), "Processing...")
                    ##### GRIP OPERATION ####
                    Motor_B_1_PWM.ChangeDutyCycle(0)
                    Motor_B_2_PWM.ChangeDutyCycle(0)
                    GPIO.output(Motor_B_1,True)
                    GPIO.output(Motor_B_2,False)
                    Motor_B_1_PWM.ChangeDutyCycle(100)
                    Motor_B_2_PWM.ChangeDutyCycle(100)
                    ##########################
                    if abs(int(moving_average)) > 440:
                        print("Current is too high!")
                        
                        break
                else:
                    print("Moving Average Current: calculating...")
                print("")
            

            except DeviceRangeError as e:
                print(f"Error: {e}")

            time.sleep(0.1)
        
        
        ##### Feedback #####
        self.gripperStopped()

    def gripperStopped(self):
        self.gui_update_callback(100, "<b>FEEDBACK DETECTED!</b>")
        #...
        ##### Init #####
        
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        GPIO.output(Motor_B_1,False)
        GPIO.output(Motor_B_2,False)
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
    
        ################
        
    def dropOperation(self):
        self.gui_update_callback(0, "Reverse...")
        #...
        time.sleep(1)
        ### DROP OPERATION ###
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        GPIO.output(Motor_B_1,False)
        GPIO.output(Motor_B_2,True)        
        Motor_B_1_PWM.ChangeDutyCycle(50)
        Motor_B_2_PWM.ChangeDutyCycle(50)
        ##########################
        time.sleep(1)
        GPIO.output(Motor_B_1,False)
        GPIO.output(Motor_B_2,False)
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)

    
    def resetOperation(self):
        time.sleep(1)
        self.gui_update_callback(0, "Waiting...")
        #...
        
        ##### Init #####
        current_readings = []
        while True:
            
            try:
                bus_voltage = ina.voltage()
                current = ina.current()
                power = ina.power()
                shunt_voltage = ina.shunt_voltage()

                current_readings.append(current)

                if len(current_readings) > max_len:
                    current_readings.pop(0)

                if len(current_readings) == max_len:
                    moving_average = sum(current_readings) / len(current_readings)
                else:
                    moving_average = None

                print(f"Bus Voltage: {bus_voltage:.3f} V")
                print(f"Shunt Voltage: {shunt_voltage:.3f} mV")
                print(f"Current: {current:.3f} mA")
                if moving_average is not None:
                    print(f"Moving Average Current: {moving_average:.3f} mA")
                    self.gui_update_callback(0, "Resetting...")
                    ##### GRIP OPERATION ####
                    Motor_B_1_PWM.ChangeDutyCycle(0)
                    Motor_B_2_PWM.ChangeDutyCycle(0)
                    GPIO.output(Motor_B_1,True)
                    GPIO.output(Motor_B_2,False)
                    Motor_B_1_PWM.ChangeDutyCycle(100)
                    Motor_B_2_PWM.ChangeDutyCycle(100)
                    ##########################
                    if abs(int(moving_average)) > 80:
                        print("Reset completed!")
                        
                        break
                else:
                    print("Moving Average Current: calculating...")
                print("")
            

            except DeviceRangeError as e:
                print(f"Error: {e}")

            time.sleep(0.1)
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        GPIO.output(Motor_B_1,False)
        GPIO.output(Motor_B_2,False)
        Motor_B_1_PWM.ChangeDutyCycle(0)
        Motor_B_2_PWM.ChangeDutyCycle(0)
        ################
    


