class SortedKeysDictionary:
    def __init__(self, dictionary = None):
        if dictionary:
            self._data = dict(dictionary)
        else:
            self._data = {}