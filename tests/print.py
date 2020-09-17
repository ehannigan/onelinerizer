import sys
import io

print()
print(1, end=' ')
print(2)

s = io.StringIO()
print(3, end=' ', file=s)
print(4, file=s)
print(repr(s.getvalue()))

def f():
    print('f')
    return sys.stdout
def g():
    print('g')
    return 'hello'
print(g(), file=f())
