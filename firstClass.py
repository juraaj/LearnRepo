class Point:
    __secretAttr = 0

    def __init__(self,x=7,y=12):
        self.x = x
        self.y = y



p = Point()

print(str(p.x) + " " + str(p.y))
print(p._Point__secretAttr)
print("hello")
