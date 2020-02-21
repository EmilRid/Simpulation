from Map import *
from Plant import *
import random
import math
import time


class Entity:
    food = 100
    nearestFood = None

    def __init__(self, name, entityX, entityY, currentMap):
        self.entityX = entityX
        self.entityY = entityY
        self.currentMap = currentMap
        self.name = name

        currentMap.entities.append(self)

    def entityIcon(self):
        return self.name[0].upper()

    def randomMove(self):
        RandomDirection = random.choice(["north", "east", "south", "west"])
        self.currentMap.content[self.entityY][self.entityX] = "."
        if RandomDirection == "north" and self.entityY != 0:
            self.entityY -= 1
        if RandomDirection == "south" and self.entityY != self.currentMap.mapY-1:
            self.entityY += 1
        if RandomDirection == "east" and self.entityX != self.currentMap.mapX-1:
            self.entityX += 1
        if RandomDirection == "west" and self.entityX != 0:
            self.entityX -= 1

    def searchFood(self):
        # Finds nearest plants
        Entity.nearestFood = None
        for plant in self.currentMap.plants:
            if Entity.nearestFood == None:
                Entity.nearestFood = plant
            if math.sqrt((plant.plantX-self.entityX)**2 + (plant.plantY-self.entityY)**2) < math.sqrt((Entity.nearestFood.plantX-self.entityX)**2 + (Entity.nearestFood.plantY-self.entityY)**2):
                Entity.nearestFood = plant

       # Walks to nearest plant
        self.currentMap.content[self.entityY][self.entityX] = "¤"
        if abs(Entity.nearestFood.plantY - self.entityY) > abs(Entity.nearestFood.plantX - self.entityX):
            if Entity.nearestFood.plantY - self.entityY < 0:
                self.move("north")
            elif Entity.nearestFood.plantY - self.entityY > 0:
                self.move("south")
        else:
            if Entity.nearestFood.plantX - self.entityX > 0:
                self.move("east")
            elif Entity.nearestFood.plantX - self.entityX < 0:
                self.move("west")

    def move(self, direction):
        Entity.food -= 1
        if direction == "none":
            if Entity.food >= 75:
                self.randomMove()

            if Entity.food < 75:
                self.searchFood()

        if direction == "north" and self.entityY != 0:
            self.entityY -= 1
        if direction == "south" and self.entityY != self.currentMap.mapY-1:
            self.entityY += 1
        if direction == "east" and self.entityX != self.currentMap.mapX-1:
            self.entityX += 1
        if direction == "west" and self.entityX != 0:
            self.entityX -= 1
