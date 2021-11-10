from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("(values is not iterable)")
    for elem in iterable:
        try:
            yield function_to_apply(elem)
        except ValueError:
            raise ValueError("(wrong value)")
        except TypeError:
            raise TypeError("(wrong type)")
        except NameError:
            raise NameError("(wrong name)")
        except ZeroDivisionError:
            raise ZeroDivisionError("(can't div by 0)")
