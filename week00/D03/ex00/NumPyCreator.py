import numpy as np
from collections.abc import Iterable


def check_dim(itr, type):

    size = -1
    for elem in itr:
        if not isinstance(elem, type):
            return True
        if size != -1:
            if size != len(elem):
                return False
        size = len(elem)
    return True


class NumPyCreator:

    def from_list(self, lst):
        if isinstance(lst, list):
            if not check_dim(lst, list):
                return None
            return np.array(lst)
        return None

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple):
            if not check_dim(tpl, tuple):
                return None
            return np.array(tpl)
        return None

    def from_iterable(self, itr):
        if isinstance(itr, Iterable):
            return list(np.array(itr))

    def from_shape(self, shape, value=0):
        if isinstance(shape, tuple):
            return np.full(shape, value)

    def random(self, shape):
        if isinstance(shape, tuple):
            return np.random.rand(shape[0], shape[1])
        return None

    def identity(self, n):
        return np.identity(n)
