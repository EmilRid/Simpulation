from Map import Map
from Entity import Entity
from Plant import Plant
from os import system, name
from time import sleep


def cls():
    _ = system("cls")


map1 = Map("map1", 25, 12)
ent1 = Entity("Jeff", 10, 5, map1)
plant1 = Plant("1", map1)
plant2 = Plant("2", map1)
map1.generateMap()

while True:
    ent1.move()
    map1.displayMap()
    if ent1.nearestFood == plant1:
        print("plant1")
    if ent1.nearestFood == plant2:
        print("plant2")
    sleep(0.5)
    cls()
