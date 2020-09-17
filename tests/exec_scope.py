g = 0
def f():
    global g
    l = 0
    exec('global g; g = 1; l = 1')
    print(g, l)
    exec('global g; g = 2; l = 2', None)
    print(g, l)
    exec('global g; g = 3; l = 3', {})
    print(g, l)
    exec('global g; g = 4; l = 4', None, None)
    print(g, l)
    exec('global g; g = 5; l = 5', None, {})
    print(g, l)
    exec('global g; g = 6; l = 6', {}, None)
    print(g, l)
    exec('global g; g = 7; l = 7', {}, {})
    print(g, l)
f()
