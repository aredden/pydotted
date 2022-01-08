import numpy as np
import pytest
from pydotted import pydot


@pytest.fixture
def d():
    return pydot({"a": 1})


@pytest.fixture
def nested():
    return pydot(
        {
            "subdoc": {
                "subsubdoc": {
                    "subsubsubdoc": [
                        {
                            "subsubsubsubdoc": [
                                [
                                    [
                                        {
                                            "_name": "n1",
                                            "_val": set(
                                                [
                                                    '{"_id": "item_id"}',
                                                    '{"_id": "item_id2"}',
                                                ]
                                            ),
                                        }
                                    ]
                                ]
                            ],
                            "_name": "subsubsubsubdoc",
                            "othertype": np.array(
                                [1,2,3,4,5,6],
                                dtype=np.float64,
                            ),
                        }
                    ]
                },
                "yes":[
                ("hi","hello"),
                ("pol","policies")
                ]
            }
        },
    )


@pytest.mark.parametrize(
    argnames=["pydt", "expected_result"], argvalues=[[pydot({"a": 1}), 1]]
)
def test_simple_dict(pydt, expected_result):
    assert pydt.a == expected_result, "{}: {}".format(__name__, pydt.a)


def test_simple_assign(d):
    d.b = d.a + 4
    assert (
        d.b == 5
    ), "Simple dict dot access works when after assigning a value using dot access."


def test_nested_dicts(d):
    d.c = {"b": object(), "a": 123}
    # prints {'a': 1, 'b': 5, 'c': {'b': <object object at 0x...>, 'a': 123}}
    assert d.c.a == 123, "Must access nested dicts correctly."


def test_correct_nested_conversion(d):
    d.a = {"e": {"f": {"h": {"i": "j"}}}}
    assert d.a.e.f.h.i == "j", "Dict's within dicts must be converted to pydot dicts."


# Still supports normal dictionary property access
def test_normal_dict_property_access(d):
    d["j"] = 20
    assert d["j"] == 20, "Normal dict access works"


# Supports nested arrays within dictionaries within arrays, (etc...) :)
def test_nested_arrays_within_dicts(d):
    d.a = {"e": {"f": {"h": {"i": "j"}}}}
    d.a.e.f.h.i = [{"a": {"b": "c"}}]
    assert (
        d.a.e.f.h.i[0].a.b == "c"
    ), "Nested dict inside of list must be supported in pydotted."


def test_nested_arrays_within_arrays(d):
    d.a = {"e": {"f": {"h": {"i": [[[{"a": {"b": "c"}}]]]}}}}
    assert (
        d.a.e.f.h.i[0][0][0].a.b == "c"
    ), "Nested array inside of array must be supported in pydotted."


def test_list_w_empty_list(d):
    d.b = [[[[[]]]]]
    assert (
        d.b[0][0][0][0] == []
    ), "Dictionary with empty list creates an item at the right depth."


def test_deeply_nested_dict_to_pydot(d):
    d.b = [[[[[{"a": {"b": 1}}]]]]]
    assert (
        d.b[0][0][0][0][0].a.b == 1
    ), "Support dicts nested deeply within arrays of more than two dimensions."


def test_fail_on_non_dict():
    with pytest.raises(TypeError):
        pydot([])


def test_pass_on_empty():
    pydot()


def test_fail_multiarg():
    with pytest.raises(TypeError):
        a = 1
        b = 2
        pydot(a, b)


def test_pass_kwargs():
    p = pydot(
        name="pydot",
        arr=[0, 1, 2, 3, 4, 5],
        nested={"a": {"b": {"c": {"d": {"e": {"f": 1}}}}}},
    )
    assert p.arr == [0, 1, 2, 3, 4, 5], "keys/names couldn't be passed as kwargs."
    assert p.name == "pydot", "keys/names couldn't be passed as kwargs."
    assert p.nested.a.b.c.d.e.f == 1, "keys/names couldn't be passed as kwargs."


def test_pass_is_dict():
    p = pydot({"arr": 1})
    assert isinstance(p, pydot) and isinstance(
        p, dict
    ), "pydot should be both a dictionary and pydot object."


def test_to_dict():
    p = pydot({"arr": [{"_name": "node1"}]})
    d = p.todict()
    assert isinstance(d, dict) and not isinstance(d, pydot)


def test_todict_nested(nested):
    p = nested
    assert p.subdoc.subsubdoc.subsubsubdoc[0].subsubsubsubdoc[0][0][0]._name == "n1"
    p = p.todict()
    nested = p["subdoc"]["subsubdoc"]["subsubsubdoc"][0]["subsubsubsubdoc"][0][0][0]
    assert nested["_name"] == "n1"
    assert type(nested) != pydot and type(nested) == dict
