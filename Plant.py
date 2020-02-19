import random

class Plant:
    def __init__(self, currentMap):
        self.currentMap = currentMap
        plantX = 0
        plantY = 0

        self.plantX = random.randint(0, currentMap.mapX-1)
        self.plantY = random.randint(0, currentMap.mapY-1)
        currentMap.plants.append(self)

    def entityIcon(self):
       return "*"