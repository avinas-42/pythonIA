from collections.abc import Iterable


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("(values is not iterable)")
    it = iter(iterable)
    value = next(it)
    for elem in it:
        try:
            value = function_to_apply(value, elem)
        except ValueError:
            raise ValueError("(wrong value)")
        except TypeError:
            raise TypeError("(wrong type)")
        except NameError:
            raise NameError("(wrong name)")
        except ZeroDivisionError:
            raise ZeroDivisionError("(can't div by 0)")
    return value
