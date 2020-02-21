from Map import Map
from Entity import Entity
from Plant import Plant
from os import system, name
from time import sleep


def cls():
    _ = system("cls")


map1 = Map("map1", 25, 25)
ent1 = Entity("Jeff", 0, 0, map1)
plant1 = Plant("none", 0, 0, map1)
plant2 = Plant("none", 0, 0, map1)
plant3 = Plant("none", 0, 0, map1)
plant4 = Plant("none", 0, 0, map1)
plant5 = Plant("none", 0, 0, map1)
plant6 = Plant("none", 0, 0, map1)
plant7 = Plant("none", 0, 0, map1)
plant8 = Plant("none", 0, 0, map1)
map1.generateMap()

while True:
    ent1.move("none")
    map1.displayMap()
    print(ent1.name, Entity.food)
    sleep(0.5)
    cls()
