import random


class Plant:
    def __init__(self, name, plantX, plantY, currentMap):
        self.currentMap = currentMap
        self.name = name
        self.plantX = plantX
        self.plantY = plantY

        if plantX == 0 and plantY == 0:
            self.plantX = random.randint(0, currentMap.mapX-1)
            self.plantY = random.randint(0, currentMap.mapY-1)
            
        currentMap.plants.append(self)

    def entityIcon(self):
        return self.name[0].upper()
