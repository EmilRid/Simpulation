import random

class Plant:
    def __init__(self, name,  currentMap):
        self.currentMap = currentMap
        self.name = name
        plantX = 0
        plantY = 0

        self.plantX = random.randint(0, currentMap.mapX-1)
        self.plantY = random.randint(0, currentMap.mapY-1)
        currentMap.plants.append(self)

    def entityIcon(self):
       return self.name[0].upper()