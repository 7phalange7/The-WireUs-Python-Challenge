# challenge 50

import numpy as np

array = np.random.randint(1,1000,size=(4,9))

split_array = np.hsplit(array,3)

print(split_array)
