import numpy as np
from PIL import Image

class ImageProcessor:
  def load(self, path):
    img = Image.open(path)
    array = np.array(img)
    print("Loading image of dimensions", array.shape[0], "x", array.shape[1])
    return array

  def display(self, array):
    print(array)