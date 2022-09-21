class Serpiente:
    pass
class Piton(Serpiente):
    pass

print(Piton.__name__, Serpiente.__name__)
print(Piton.__bases__[0].__name__, Piton.__name__)