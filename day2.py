records = [
    ('foo', 13, 12),
    ('bar', 'hello'),
    ('foo', 3, 23)
    ]

def foo(x, y):
    print("foo", x, y)

def bar(s):
    print("bar", s)

for tag, *args in records:
    if tag=='foo':
        foo(*args)
    elif tag=='bar':
        bar(*args)
        
