from typing import Any


class pydot(dict):
    """
    A dictionary that can get attribute (x.y) access, including nested dicts.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if type(__value) == dict:
            __value = pydot(__value)
            for __key in __value:
                __value.__setattr__(__key, __value[__key])
        self.__setitem__(__name, __value)

    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
