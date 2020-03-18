from Map import Map
from Entity import Entity
from Plant import Plant
from os import system, name
from time import sleep


def cls():
    _ = system("cls")


map1 = Map("map1", 20, 20)
ent1 = Entity("Jeff", 0, 0, map1)
ent2 = Entity("test", 0, 0, map1)
plant1 = Plant("none", 0, 0, map1)
plant2 = Plant("none", 0, 0, map1)
plant3 = Plant("none", 0, 0, map1)
plant4 = Plant("none", 0, 0, map1)
map1.generateMap()

while True:
    ent1.move("none")
    ent2.move("none")
    map1.displayMap()
    for ent in map1.entities:
        print(ent.food, end="")
    sleep(0.5)
    cls()
