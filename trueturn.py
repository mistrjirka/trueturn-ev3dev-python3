#!/usr/bin/env python3

from ev3dev.ev3 import GyroSensor, LargeMotor
from time import sleep

#main class
class TrueTurn:
	def __init__(self, motor1Port, motor2Port, gyroPort=None, speed = 200): #init
		self.speed = speed
		if GyroSensor == None:
			self.GS = GyroSensor(gyroPort)
		self.M1 = LargeMotor(motor1Port)
		self.M2 = LargeMotor(motor2Port)
	def turn(degrees):
		multiplayer = -1
		if degrees > 0:
			multiplayer = 1 
		gy.mode='GYRO-ANG'
		angle = self.GS.value()
		run = false
		while angle - self.GS.value() != degrees:
			if run == false:
				self.M1.run_forever(speed_sp=self.speed * multiplayer)
				self.M2.run_forever(speed_sp=self.speed * multiplayer * -1)
			sleep(0.01)
		self.M2.stop()
		self.M1.stop()
		return true
				
