class Human:
    humans = []
    totalHumans = 0
    def __init__(self, name, age, x, y):
        self.name = name
        self.age = age
        self.x = x 
        self.y = y
        Human.totalHumans += 1
        Human.humans.append(Human)

    def getInfo(self):
        return self.name, self.age, self.x, self.y
    
    def setInfo(self, name, age):
        self.name = name
        self.age = age

class Map:
    def __init__(self, xValue, yValue):
        self.xValue = xValue
        self.yValue = yValue
    
    def getArea(self, humans):
        for n in range(self.yValue):
            for i in range(self.xValue):
                for human in humans:
                    if human.y == n and human.x == i:
                        print(human.name[0].upper(), end = " ")
                print(" ", end=" ")
            print("I")