from Map import *
from Plant import *
import random


class Entity:
    food = 100
    nearestFood = []

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
        for entity in self.currentMap.entities:
            if entity is Plant:
                if (entity.entityX + entity.entityY) - (self.entityX + self.entityY) < 15:
                    self.nearestFood.append(entity)
                    break

    def move(self):
        Entity.food -= 1

        if Entity.food >= 75:
            self.randomMove()

        elif Entity.food < 75:
            self.searchFood()
