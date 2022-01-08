from typing import Any


class pydot(dict):
    """
    A dictionary that can get attribute (x.y) access, including nested dicts.
    """

    def __init__(self, *args, **kwargs) -> "pydot":
        dict.__init__(self, *args, **kwargs)
        # Dict will always throw error if num args > 1, so we are safe to
        # check if there is only one type of arg.
        args = args[0] if type(args) == tuple and len(args) == 1 else args
        if type(args) == list:
            raise TypeError("Cannot instantiate a pydot with list as argument.")
        for k, v in self.items():
            self.__setattr__(k, v)

    def __check_nested_list(self, __list: list) -> list:
        if len(__list) == 0:
            return __list
        for i, _item in enumerate(__list):
            if type(_item) == list:
                __list[i] = self.__check_nested_list(_item)
            elif type(_item) == dict:
                __next = pydot(_item)
                for __key in _item:
                    __next.__setattr__(__key, _item[__key])
                __list[i] = __next
        return __list

    def __setattr__(self, __name: str, __value: Any) -> None:
        if type(__value) == dict:
            __value = pydot(__value)
            for __key in __value:
                __value.__setattr__(__key, __value[__key])
        elif type(__value) == list:
            __value = self.__check_nested_list(__value)
        self.__setitem__(__name, __value)

    def __todict_nested(self, __obj):
        if type(__obj) == pydot:
            return __obj.todict()
        elif type(__obj) == list:
            for i, v in enumerate(__obj):
                __obj[i] = self.__todict_nested(v)
            return __obj
        else:
            return __obj

    def todict(self) -> dict:
        """Returns a dictionary containing the converted object and nested objects.

        Returns:
            dict: A dictionary containing the converted pydot object and the
                nested objects.
        """
        d = {}
        for k, v in self.items():
            if type(v) == pydot:
                v = v.todict()
            elif type(v) == list:
                v = self.__todict_nested(v)
            d[k] = v
        return d

    __getattr__ = dict.get
    __delattr__ = dict.__delitem__


___ALL___ = ["pydot"]
