import os
import pickle


class Cache(object):

    PATH = os.path.join('.cache', 'coverage.space')

    def __init__(self):
        self._data = {}
        self._load()

    def _load(self):
        try:
            with open(self.PATH, 'r') as fin:
                data = pickle.load(fin)
        except (IOError, KeyError, IndexError):
            pass
        else:
            if isinstance(data, dict):
                self._data = data

    def _store(self):
        directory = os.path.dirname(self.PATH)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(self.PATH, 'w') as fout:
            pickle.dump(self._data, fout)

    def set(self, url, data, response):
        slug = self._slugify(url, data)
        self._data[slug] = response
        self._store()

    def get(self, url, data):
        slug = self._slugify(url, data)
        return self._data.get(slug)

    @staticmethod
    def _slugify(url, data):
        return (url, hash(frozenset(data.items())))
