from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("elon_canaGAN.png")
# Output
# Loading image of dimensions 200 x 200
from ColorFilter import ColorFilter

cf = ColorFilter()
arr = cf.to_red(arr)
imp.display(arr)
# cf.to_green(arr)
# cf.to_red(arr)
# cf.to_blue(arr)
# cf.to_celluloid(arr)
# cf.to_grayscale(arr, 'm')
# cf.to_grayscale(arr, 'weighted', [0.2, 0.3, 0.5])