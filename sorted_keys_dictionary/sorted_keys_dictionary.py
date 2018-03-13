class SortedKeysDictionary:
    def __init__(self, dictionary = None):
        if dictionary:
            self._data = dict(dictionary)
        else:
            self._data = {}

    # Getter and setter

    def get(self, key):
        return self._data[key]
    
    def set(self, key, value):
        self._data[key] = value

    # Iterable
    def __iter__(self):
        # Return a generator that sorts data
        for item in sorted(self._data.__iter__()):
            yield item

    # Container. Not needed unless we don't want to test issubclass(SortedKeysDictionary, Container).
    def __contains__(self, key):
        return key in self._data

    # Sized
    def __len__(self):
        return len(self._data)