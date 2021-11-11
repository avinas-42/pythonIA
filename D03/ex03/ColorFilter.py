import numpy as np
import copy
class ColorFilter:
    def invert(self, array):
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
        

    def to_blue(self, array):
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

    def to_green(self, array):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None 
        ret = copy.deepcopy(array)
        for line in ret:
            for pixel in line:
                pixel[0] *= 0.01
                pixel[2] *= 0.01
        return ret

    def to_red(self, array):
        if not isinstance(array, (np.ndarray, np.generic)):
            return None
        if array.shape[2] == 4:
            alpha = array[:, :, 3]
            tmp = array - self.to_green(array)
            tmp = tmp - self.to_blue(array)
            tmp[:,:,3] = alpha
        else:
            tmp = array - self.to_green(array)
            tmp = tmp - self.to_blue(array)
            
        return tmp