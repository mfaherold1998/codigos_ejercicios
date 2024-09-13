
#None = object()
from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        self._slots = capacity * [None]

    def __len__(self):
        return len(self.pairs)
    
    def __setitem__(self, key, value):
        self._slots[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._slots[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value
    
    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
        
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __delitem__(self, key):
        if key in self:
            self._slots[self._index(key)] = None
        else:
            raise KeyError(key)
    
    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"
    
    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"
    
    @property
    def pairs(self):
        return {pair for pair in self._slots if pair}

    @property
    def values(self):
        return [pair.value for pair in self.pairs]
    
    @property
    def keys(self):
        return {pair.key for pair in self.pairs}
    
    @property
    def capacity(self):
        return len(self._slots)
    
    def _index(self, key):
        return hash(key) % self.capacity
    
    @classmethod
    # Esto significa que el método puede ser llamado directamente sobre la clase y no sobre una instancia de la clase.
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
    

# all() is quite verbose
# La función all() toma la secuencia de valores booleanos producida por 
# la expresión generadora y devuelve True solo si todos los valores son True.
def have_same_elements(list1, list2):
    return all(element in list1 for element in list2)

#Lo dejamos aqui: https://realpython.com/python-hash-table/#test-the-equality-of-hash-tables