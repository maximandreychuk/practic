class Singleton:
    instance = None
    def __init__(self):
        if Singleton.instance is not None:
            raise Exception("EXCEPTION")
        else:
            Singleton.instance = self


s1 = Singleton()
s2 = Singleton()

print(s1, s2)
