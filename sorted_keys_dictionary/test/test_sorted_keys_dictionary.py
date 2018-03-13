from sorted_keys_dictionary.sorted_keys_dictionary import SortedKeysDictionary

class TestSortedKeysDictionary:
    def test_initializer_accepts_dictionary(self):
        # Data should be a copy, not the original
        s1 = SortedKeysDictionary()
        assert s1._data == {}
        
        d = {"x": 1, "y": "thirty five"}
        s2 = SortedKeysDictionary(d)
        assert s2._data == d
        assert s2._data is not d # it's a copy, not a reference
