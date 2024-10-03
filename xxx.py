class Foo(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


obj1 = Foo("ITdepart")
print(obj1)  #
obj2 = Foo("saledepart")
print(obj2)  # 
