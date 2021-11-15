import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given
        by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(array, (np.ndarray, np.generic)) and \
                isinstance(dim, tuple) and len(dim) == 2 and  \
                isinstance(dim[0], int) and isinstance(dim[1], int) and \
                isinstance(position, tuple) and len(position) == 2 and \
                isinstance(position[0], int) and isinstance(position[1], int):
            array = array[position[0]:dim[0] + position[0],
                          position[1]:dim[1]+position[1]]
            return array
        return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified
        axis (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than
        the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        if axis == 0 or axis == 1:
            # tmpaxis = 0 if axis == 1 else 1
            remove_list = list(
                map(lambda x: x - 1, np.arange(n, array.shape[axis], n)))
            return np.delete(array, remove_list, axis=axis)
        return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(array, (np.ndarray, np.generic)):
            if axis == 1:
                return np.tile(array, n)
            elif axis == 0:
                return np.repeat(array, n, axis=0)
        return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array.
        The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if isinstance(array, (np.ndarray, np.generic)) and \
                isinstance(dim, tuple) and len(dim) == 2 and  \
                isinstance(dim[0], int) and isinstance(dim[1], int):
            array = np.tile(array, dim[1])
            array = np.repeat(array, dim[0], axis=0)
            return array
        return None
        pass
