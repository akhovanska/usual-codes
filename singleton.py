class Singleton:

    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, c):
        self._c = c

    def __str__(self):
        return str(self._c)


s = Singleton(1)
print("object created", s)
s1 = Singleton(2)
print("object created", s1)

print(Singleton.__dict__)
