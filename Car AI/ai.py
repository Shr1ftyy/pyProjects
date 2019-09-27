import pygame
import math
import time 
import os
import game
from game import Car 
from game import Game

class AI:
	def control():
		car = game.Car(0,0)
		dt = Game.clock.get_time() / 1000
		if car.x < 1280 and car.x != 1000:
			if car.velocity.x < 0:
				car.acceleration = car.brake_deceleration
			else:
				car.acceleration += 1 * dt