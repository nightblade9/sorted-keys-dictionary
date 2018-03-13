from sorted_keys_dictionary.sorted_keys_dictionary import SortedKeysDictionary

class TestSortedKeysDictionary:
    def test_initializer_accepts_dictionary(self):
        s1 = SortedKeysDictionary()
        
        d = {"x": 1, "y": "thirty five"}
        s2 = SortedKeysDictionary(d)