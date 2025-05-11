import numpy as np
a = np.random.rand(50).astype(np.int64)
np.save("graderArrInt.npy", a)
b = np.random.rand(50).astype(np.float64)
np.save("graderArrFloat.npy", b)