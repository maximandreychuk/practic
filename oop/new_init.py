class Prodict:
    id_counter = 1
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls.id_counter
        cls.id_counter += 1
        return instance

    def __init__(self, name):
        self.name = name


pr1 = Prodict("obj")
pr2 = Prodict("foo")
print(pr1.id, pr2.id)
