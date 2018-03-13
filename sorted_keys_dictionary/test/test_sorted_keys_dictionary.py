from sorted_keys_dictionary.sorted_keys_dictionary import SortedKeysDictionary
from collections import Container, Iterable, Sized

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

    def test_class_is_iterable(self):
       assert issubclass(SortedKeysDictionary, Iterable)

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

    def test_class_implements_container_protocol(self):
        assert issubclass(SortedKeysDictionary, Container)

    def test_in_returns_true_for_existing_keys(self):
        s = SortedKeysDictionary({"cats": "yes please", "dogs": "no thanks"})
        assert "cats" in s
        assert "tigers" not in s

    def test_class_is_sized(self):
        assert issubclass(SortedKeysDictionary, Sized)

    def test_len_returns_number_of_unique_keys(self):
        s = SortedKeysDictionary({"one": 1, "two": 2, "three": 3})
        s.set("two", 22)
        assert len(s) == 3

    def test_class_is_sequence(self): pass # TODO: fill in at the end

    def test_index_slicing_returns_items(self):
        s = SortedKeysDictionary({"one": 1, "two": 2, "three": 3})
        assert s[0] == "one"
        assert s[1] == "two"
    
    def test_positive_slicing_returns_subset(self):
        s = SortedKeysDictionary({"one": 1, "two": 2, "three": 3})
        actual = s[0:1]
        assert len(actual) == 1
        assert actual[0] == "one"
    
    def test_partial_slicing_returns_subset(self):
        s = SortedKeysDictionary({"one": 1, "two": 2, "three": 3, "four": 4})      
        suffix = s[:2]
        assert len(suffix) == 2
        assert suffix[0] == "one"
        assert suffix[1] == "two"

        prefix = s[2:]
        assert len(prefix) == 2
        assert prefix[0] == "three"
        assert prefix[1] == "four"
    
    def test_slicing_returns_copy_without_indicies(self):
        s = SortedKeysDictionary({"one": 1, "two": 2, "three": 3, "four": 4})
        actual = s[:]
        assert len(actual) == 4
        assert actual[0] == "one"
        assert actual[1] == "two"
        assert actual[2] == "three"
        assert actual[3] == "four"
        
        