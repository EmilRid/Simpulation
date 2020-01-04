from Objects import Human
from Objects import Map

human1 = Human("Example", 15, 2, 6)
human2 = Human("test3", 15, 6, 7)
newMap = Map(10, 10)

newMap.getArea([human1, human2])