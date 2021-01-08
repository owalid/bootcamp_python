import numpy as np

class ScrapBooker:
  def crop(self, array, dimensions, position=(0,0)):
    return array[dimensions[0]:dimensions[0]+position[0], dimensions[1]:dimensions[1]+position[1]]

  def thin(self, array, n, axis):
    return np.delete(array, list(range(0, array.shape[0]), n), axis=axis)

  def juxtapose(self, array, n, axis):
    result = np.copy(array)
    for _ in range(n):
      result = np.concatenate((result, np.copy(array)), axis=axis)
    return result