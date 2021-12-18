from pydotdict import dotdict

d = dotdict({"a": 1})

print(d.a)
# prints 1

d.b = d.a + 4

print(d.b)
# prints 5

d.c = {"b": object(), "a": 123}

print(d)
# prints {'a': 1, 'b': 5, 'c': {'b': <object object at 0x...>, 'a': 123}}

print(d.c.a)
# prints 123

d.a = {"e": {"f": {"h": {"i": "j"}}}}

print(d.a.e.f.h.i)
# prints "j"