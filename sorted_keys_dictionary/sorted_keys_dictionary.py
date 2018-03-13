class SortedKeysDictionary:
    def __init__(self, dictionary = None):
        if dictionary:
            self._data = dict(dictionary)
        else:
            self._data = {}

    def get(self, key):
        return self._data[key]
    
    def set(self, key, value):
        self._data[key] = value