from sorted_keys_dictionary.sorted_keys_dictionary import SortedKeysDictionary
from collections import Iterable

class TestSortedKeysDictionary:
    def test_initializer_accepts_dictionary(self):
        # Data should be a copy, not the original
        s1 = SortedKeysDictionary()
        assert s1._data == {}
        
        d = {"x": 1, "y": "thirty five"}
        s2 = SortedKeysDictionary(d)
        assert s2._data == d
        assert s2._data is not d # it's a copy, not a reference

    def test_getter_gets_initializer_values(self):
        # Don't use indexing because it might not be implemented yet
        s = SortedKeysDictionary({"name": "test", "age": 271})
        assert s.get("name") == "test"
        assert s.get("age") == 271
    
    def test_getter_gets_set_values_overriding_previous(self):
        s = SortedKeysDictionary()
        s.set("monkeys", 37)
        s.set("apples", "seven")
        assert s.get("monkeys") == 37
        assert s.get("apples") == "seven"

        s.set("monkeys", 99)
        assert s.get("monkeys") == 99

    #def test_class_is_iterable(self):
    #    s = SortedKeysDictionary()
    #    assert issubclass(s, Iterable)

    def test_class_is_iterable_and_sorted(self):
        s = SortedKeysDictionary({"b": 7, "a": 1})
        actual = [item for item in s]

        assert actual[0] == "a"
        assert actual[1] == "b"

    def test_adding_elements_maintains_sorted_order(self):
        s = SortedKeysDictionary({"d": 7, "b": 1})
        s.set("c", 0)
        
        actual = [item for item in s]
        assert actual[0] == "b"
        assert actual[1] == "c"
        assert actual[2] == "d"