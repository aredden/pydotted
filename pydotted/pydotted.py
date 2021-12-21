from typing import Any


class pydot(dict):
    """
    A dictionary that can get attribute (x.y) access, including nested dicts.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        for k,v in self.items():
            self.__setattr__(k, v)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if type(__value) == dict:
            __value = pydot(__value)
            for __key in __value:
                __value.__setattr__(__key, __value[__key])
        elif type(__value) == list:
            for i,__v in enumerate(__value):
                if type(__v) == dict:
                    __next = pydot(__v)
                    for __key in __v:
                        __next.__setattr__(__key, __v[__key])
                    __value[i] = __next
        self.__setitem__(__name, __value)

    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
