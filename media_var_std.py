import numpy as np

def calculate(list):
  
  #Se a lista conter 9 numeros, faça:
  if len(list) == 9:
    array = np.array(list).reshape(3,3)
    calculations = {
    "mean":[array.mean(axis=0).tolist(), 
            array.mean(axis=1).tolist(),
            array.mean()],
    "variance":[array.var(axis=0).tolist(),
                array.var(axis=1).tolist(),
                array.var()],
    "standard deviation":[array.std(axis=0).tolist(),
                          array.std(axis=1).tolist(),
                          array.std()],
    "max": [array.max(axis=0).tolist(),
            array.max(axis=1).tolist(),
            array.max()],
    "min":[array.min(axis=0).tolist(),
           array.min(axis=1).tolist(),
           array.min()],
    "sum":[array.sum(axis=0).tolist(),
           array.sum(axis=1).tolist(),
           array.sum()]
    }
  
  #senão
  else:
    raise ValueError("List must contain nine numbers.")
  


  return calculations