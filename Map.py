class Map:
    content = []
    entities = []
    plants = []

    def __init__(self, mapName, mapX, mapY):
        self.mapName = mapName
        self.mapX = mapX
        self.mapY = mapY

    def generateMap(self):
        for y in range(self.mapY):
            Map.content.append([])
            for x in range(self.mapX):
                Map.content[y].append("_")

    def displayMap(self):
        for plant in Map.plants:
            try:
                Map.content[plant.plantY][plant.plantX] = plant.entityIcon()
            except:
                pass
        for entity in Map.entities:
            try:
                Map.content[entity.entityY][entity.entityX] = entity.entityIcon()
            except:
                pass

        for x in Map.content:
            print(*x, sep="")
