import numpy as np


def calculate(list):
  if len(list) == 9:
    x = np.array(list).reshape(3, 3)
    mean = [x.mean(0).tolist(), x.mean(1).flatten().tolist(), x.mean()]
    var = [x.var(0).tolist(), x.var(1).flatten().tolist(), x.var()]
    std = [x.std(0).tolist(), x.std(1).flatten().tolist(), x.std()]
    max = [x.max(0).tolist(), x.max(1).flatten().tolist(), x.max()]
    min = [x.min(0).tolist(), x.min(1).flatten().tolist(), x.min()]
    sum = [x.sum(0).tolist(), x.sum(1).flatten().tolist(), x.sum()]
    calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
    }
  else:
    raise ValueError("List must contain nine numbers.")

  return calculations
