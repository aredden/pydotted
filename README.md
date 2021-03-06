# PyDotted

![coverage](https://github.com/aredden/pydotted/blob/main/coverage.svg)

A very simple low code footprint dictionary with dot notation attribute (x.y) access, including nested dicts.

## Installation:

<strong> From git: </strong>
```bash
pip install git+https://github.com/aredden/pydotted.git
```

<strong>From pypi:</strong>
```bash
pip install pydotted
```

## Examples & Usage:

```python
from pydotted import pydot

d = pydot({"a": 1})

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


# Still supports normal dictionary property access
d["j"] = 20

print(d.j)
# prints 20

d.a.e.f.h.i = [{"a": {"b": "c"}}]

# Supports nested lists within dictionaries within lists, (etc...) :)
print(d.a.e.f.h.i[0].a.b)
# prints "c"

# Supports deeply nested lists
d.b = [[[[[{"a":{"b":1}}]]]]]
print(d.b[0][0][0][0][0].a.b)
# prints 1

```

### Updates as of 1/8/22

**New Method:** `todict()`
> Returns a non-pydot dictionary containing the converted object and nested objects.