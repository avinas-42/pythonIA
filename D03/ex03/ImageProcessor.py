import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        try:
            image = plt.imread(path)
            shape = image.shape
            if len(shape) > 1:
                large = shape[0]
                length = shape[1]
            print(f'Loading image of dimensions {large} x {length}')
            return image
        except FileNotFoundError:
            print("Exception: FileNotFoundError --\
 strerror: No such file or directory")
            return None
        except (OSError, SyntaxError):
            print("Exception: OSError -- strerror: None")
            return None

    def display(self, arr):
        plt.imshow(arr)
        plt.axis('off')
        plt.show()
