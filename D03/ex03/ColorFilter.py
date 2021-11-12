import numpy as np
import copy


class ColorFilter:

    @staticmethod
    def invert(array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        for line in array:
            for pixel in line:
                for color in range(3):
                    pixel[color] = 1 - pixel[color]
        return array

    @staticmethod
    def to_blue(array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        size = (array.shape[0], array.shape[1])
        red = np.zeros(size)
        green = np.zeros(size)
        blue = array[:, :, 2]

        if array.shape[2] == 4:
            alpha = array[:, :, 3]
            ret = np.dstack((red, green, blue, alpha))
        else:
            ret = np.dstack((red, green, blue))

        return ret
        # if isinstance(array, (np.ndarray, np.generic)):
        #     for line in array:
        #         for pixel in line:
        #             pixel[0] = 0
        #             pixel[1] = 0
        #     return array

    @staticmethod
    def to_green(array):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        ret = copy.deepcopy(array)
        for line in ret:
            for pixel in line:
                pixel[0] *= 0.01
                pixel[2] *= 0.01
        return ret

    @staticmethod
    def to_red(array):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        if array.shape[2] == 4:
            alpha = array[:, :, 3]
            tmp = array - ColorFilter.to_green(array)
            tmp = tmp - ColorFilter.to_blue(array)
            tmp[:, :, 3] = alpha
        else:
            tmp = array - ColorFilter.to_green(array)
            tmp = tmp - ColorFilter.to_blue(array)

        return tmp

    @staticmethod
    def to_celluloid(array):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        ret = np.array(array)
        colors = np.linspace(0.0, 1.0, num=5, endpoint=True)[::-1]
        for i in colors:
            indexes = array >= i
            array[indexes] = -1
            ret[indexes] = i
        return ret

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        ret = np.array(array)
        if filter in ['m', 'mean']:
            for line in ret:
                for pixel in line:
                    mean = np.sum(pixel) / 3
                    pixel[0] = mean
                    pixel[1] = mean
                    pixel[2] = mean
            return ret
        elif filter in ['w', 'weight']:
            rgb_weigth = [-1, -1, -1]
            cpt = 0
            if len(kwargs.items()) != 3:
                return None
            for key, value in kwargs.items():
                rgb_weigth[cpt] = value
                cpt += 1
            if(sum(rgb_weigth) != 1):
                return None
            for line in ret:
                for pixel in line:
                    pixel[0] *= rgb_weigth[0]
                    pixel[1] *= rgb_weigth[1]
                    pixel[2] *= rgb_weigth[2]
                    pixeltmp = pixeltmp = [pixel[0], pixel[1], pixel[2]]
                    mean = np.sum(pixeltmp) / 3
                    pixel[0] = mean
                    pixel[1] = mean
                    pixel[2] = mean
            return ret
        else:
            return None
