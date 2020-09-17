import sys

def trace(msg, value):
    print(msg)
    return value

print(trace('print arg 0', 0), trace('print arg 1', 1), end=' ')
print(trace('print arg 2', 2), trace('print arg 3', 3))
print(trace('print arg 4', 4), trace('print arg 5', 5), end=' ', file=trace('print file 0', sys.stdout))
print(trace('print arg 6', 6), trace('print arg 7', 7), file=trace('print file 1', sys.stdout))
