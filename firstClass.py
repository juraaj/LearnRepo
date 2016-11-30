class Point:

    __secretAttr = 0

    def __init__(self, x=7, y=12):
        self.x = x
        self.y = y
        self.__secretAttr = 1

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from_another(self, another):
        return ((self.x - another.x) ** 2 + (self.y - another.y) ** 2) ** 0.5

    def print_info(self):
        print(self.x + ", " + self.y)


p = Point()
print(p.__dict__)
