from Map import Map
from Entity import Entity
from Plant import Plant
from os import system, name
from time import sleep 
def cls():
    _ = system("cls")

map1 = Map("map1", 20, 10)
ent1 = Entity("Emil", 0, 0, map1)
ent2 = Entity("Nicolo", 0, 0, map1)
ent3 = Entity("Andrea", 0, 0, map1)
ent4 = Entity("Jeff", 10, 5, map1)
plant1 = Plant(map1)
plant2 = Plant(map1)
plant3 = Plant(map1)
plant4 = Plant(map1)
plant5 = Plant(map1)
plant6 = Plant(map1)
plant7 = Plant(map1)
plant8 = Plant(map1)
plant9 = Plant(map1)
plant10 = Plant(map1)
plant11 = Plant(map1)
plant12 = Plant(map1)
map1.generateMap()

while True:
    ent4.move()
    ent1.move()
    ent2.move()
    ent3.move()
    map1.displayMap()
    sleep(0.5)
    cls()