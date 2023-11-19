from ctypes import byref, c_bool, c_size_t

from hash_set import lib


class HashSet:
    def __init__(self):
        self.obj = lib.hash_set_new()

    def __del__(self):
        lib.hash_set_delete(self.obj)

    def contains(self, item):
        result = c_bool()

        if lib.hash_set_contains(self.obj, item, byref(result)) < 0:
            raise ValueError
        else:
            return result.value

    def insert(self, item):
        result = c_bool()

        if lib.hash_set_insert(self.obj, item, byref(result)) < 0:
            raise ValueError
        else:
            return result.value

    def collect(self):
        result = (c_size_t * self.len())()

        if lib.hash_set_collect(self.obj, byref(result)) < 0:
            raise ValueError
        else:
            return list(result)

    def len(self):
        result = c_size_t()

        if lib.hash_set_len(self.obj, byref(result)) < 0:
            raise ValueError
        else:
            return result.value
