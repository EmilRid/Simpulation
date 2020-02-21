from Map import Map
from Entity import Entity
from Plant import Plant
from os import system, name
from time import sleep


def cls():
    _ = system("cls")


map1 = Map("map1", 30, 7)
ent1 = Entity("Jeff", 0, 0, map1)
plant1 = Plant("1", 29, 6, map1)
map1.generateMap()

while True:
    ent1.move("none")
    map1.displayMap()
    sleep(0.5)
    cls()
