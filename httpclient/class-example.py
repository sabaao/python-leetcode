class Circle:
    PI = 3.14
    def __init__(self,r=1):
        self.__radius = r
    
    def getRadius(self):
        return self.__radius
    
    def getArea(self):
        return self.PI * self.__radius * self.__radius

c1 = Circle()
print("c1 半徑: {} ".format(c1.getRadius())) # c1 半徑: 1
    
c2 = Circle(10)
print("c2 半徑: {}".format(c2.getRadius())) # c2 半徑: 10
print("c2 圓面積: {}".format(c2.getArea())) # c2 圓面積: 314.0