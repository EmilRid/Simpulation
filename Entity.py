from Map import *
from Plant import *
import random
import math
import time


class Entity:

    def __init__(self, name, entityX, entityY, currentMap):
        self.entityX = entityX
        self.entityY = entityY
        self.currentMap = currentMap
        self.name = name
        self.food = 100
        self.nearestFood = None
        self.foodIncrement = 1

        currentMap.entities.append(self)

    def entityIcon(self):
        return self.name[0].upper() + " "

    def die(self):
        try:
            self.currentMap.content[self.entityY][self.entityX] = "  "
            self.currentMap.entities.remove(self)
            self.foodIncrement = 0
            del self
        except:pass

    def randomMove(self):
        RandomDirection = random.choice(["north", "east", "south", "west"])
        self.currentMap.content[self.entityY][self.entityX] = "  "
        if RandomDirection == "north" and self.entityY != 0:
            self.move("north")
        if RandomDirection == "south" and self.entityY != self.currentMap.mapY-1:
            self.move("south")
        if RandomDirection == "east" and self.entityX != self.currentMap.mapX-1:
            self.move("east")
        if RandomDirection == "west" and self.entityX != 0:
            self.move("west")

    def searchFood(self):
        try:
            # Finds nearest plants
            self.nearestFood = None
            for plant in self.currentMap.plants:
                if self.nearestFood == None:
                    self.nearestFood = plant
                if math.sqrt((plant.plantX-self.entityX)**2 + (plant.plantY-self.entityY)**2) < math.sqrt((self.nearestFood.plantX-self.entityX)**2 + (self.nearestFood.plantY-self.entityY)**2):
                    self.nearestFood = plant

        # Walks to nearest plant
            self.currentMap.content[self.entityY][self.entityX] = "  "
            if abs(self.nearestFood.plantY - self.entityY) > abs(self.nearestFood.plantX - self.entityX):
                if self.nearestFood.plantY - self.entityY < 0:
                    self.move("north")
                elif self.nearestFood.plantY - self.entityY > 0:
                    self.move("south")

            else:
                if self.nearestFood.plantX - self.entityX > 0:
                    self.move("east")
                elif self.nearestFood.plantX - self.entityX < 0:
                    self.move("west")
                
            if self.nearestFood.plantX == self.entityX and self.nearestFood.plantY == self.entityY:
                self.food += 25
                self.nearestFood.eaten()
        
        except:self.randomMove()


    def move(self, direction):
        self.food -= self.foodIncrement
        if direction == "none":
            if self.food >= 80:
                self.randomMove()

            if self.food < 80:
                self.searchFood()
            
            if self.food < 0:
                self.die()

        if direction != "none":
            if direction == "north" and self.entityY != 0:
                self.entityY -= 1
            if direction == "south" and self.entityY != self.currentMap.mapY-1:
                self.entityY += 1
            if direction == "east" and self.entityX != self.currentMap.mapX-1:
                self.entityX += 1
            if direction == "west" and self.entityX != 0:
                self.entityX -= 1
