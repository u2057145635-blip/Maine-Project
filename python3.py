import numpy as np
from iodata import read_checkpoint, read_txt, write_checkpoint, write_txt

arr = np.array([1.0, 2.5, 3.8])

# Checkpoint test
write_checkpoint("test.h5", "my_data", arr)
loaded_chk = read_checkpoint("test.h5", "my_data")
print("Checkpoint match:", np.allclose(arr, loaded_chk))

# Text file test
write_txt("test.txt", arr)
loaded_txt = read_txt("test.txt")
print("Text file match:", np.allclose(arr, loaded_txt))
