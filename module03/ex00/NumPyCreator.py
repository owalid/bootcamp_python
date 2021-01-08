import numpy as np

class NumPyCreator:

  def from_list(self, lst):
    return np.array(lst)
  
  def from_tuple(self, tpl):
    return np.asarray(tpl)
  
  def from_iterable(self, itr):
    return np.fromiter(itr)
  
  def from_shape(self, shape, value=0):
    return np.full(shape, value)
  
  def random(self, shape):
    return np.random.random_sample(shape)

  def identity(self, n):
    return np.eye(n)