class M(type):
    __getattribute__ = None

class G(object, metaclass=M):
    __getattribute__ = None
    def __get__(self, instance, owner):
        return lambda other: 'pass'

class C(object, metaclass=M):
    __getattribute__ = None
    __iadd__ = G()

o = C()
o.__iadd__ = None
o += 1
print(o)
