class M(type):
    def __init__(cls, name, bases, dct):
        print('metaclass')
        super(M, cls).__init__(name, bases, dct)

class C(metaclass=M):
    pass

class C(object, metaclass=M):
    pass

__metaclass__ = M

class C:
     pass
