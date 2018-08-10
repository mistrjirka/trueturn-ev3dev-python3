#!/usr/bin/env python3

from ev3dev.ev3 import GyroSensor, LargeMotor
from time import sleep
import math

#main class
class TrueTurn:
	def __init__(self, motor1Port, motor2Port, gyroPort=None, speed = 200, tolerance = 0.05): #init
		self.tolerance = tolerance
		self.speed = speed
		if GyroSensor != None:
			self.GS = GyroSensor(gyroPort)
		else:
			self.GS = GyroSensor()
		self.M1 = LargeMotor(motor1Port)
		self.M2 = LargeMotor(motor2Port)
	def turn(self, degrees):
		multiplayer = -1
		if degrees > 0:
			multiplayer = 1
		self.GS.mode='GYRO-ANG'
		angle = self.GS.value()
		run = False
		while True:
			if run == False:
				self.M1.run_forever(speed_sp=self.speed * multiplayer)
				self.M2.run_forever(speed_sp=self.speed * multiplayer * -1)
			if angle - self.GS.value() not in range(math.ceil(degrees - self.tolerance * degrees),math.ceil(degrees + self.tolerance * degrees)):
				self.M2.stop()
				self.M1.stop()
				break
			sleep(0.002)
			print(self.GS.value())
			print(str(angle - self.GS.value()) + " " + str(math.ceil(degrees - self.tolerance * degrees)) + " " + str(math.ceil(degrees + self.tolerance * degrees)))
		return true
